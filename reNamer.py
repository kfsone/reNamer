import os
import re
import wx

from appframe import AppFrame
from wx import App


class ReNamerFrame(AppFrame):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # Directory currently selected by user.
        self.m_curPath       = None

        # List of filenames in curPath on disk.
        self.m_diskNames     = []

        # Names as the patterns would affect them.
        self.m_newNames      = []

        # Are the patterns valid?
        self.m_validFromRe   = False
        self.m_validPatterns = False


    def setTextColor(self, ctrl, color):

        ctrl.SetForegroundColour(color)
        if color == wx.RED:
            ctrl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INFOBK))
        else:
            ctrl.SetBackgroundColour(wx.NullColour)


    def validateRegexFields(self, complete=False):
        """
        Validate the regex patterns, but only partially while the user
        is still typing.

        Because the 'from' pattern will be where the user specifies captures,
        changing it also requires re-validating the substitution pattern.

        However if the user is still typing (as opposed to hitting enter to
        complete the input) we do the minimal amount of work necessary, i.e
        we just set the colors back to neutral and disable the Apply button.

        TODO: Only validate the 'from' box when that is what changed.

        :param complete: True when the user hits enter and has completed their
                        input, otherwise False (do less work).
        """

        # Assume the patterns aren't valid.
        self.m_validFromRe   = False
        self.m_validPatterns = False

        ### Validate the 'from' pattern
        #
        regexCtl = self.m_reFromCtl
        subsCtl  = self.m_reToCtl

        regex, subs = regexCtl.Value, subsCtl.Value

        regColor, subColor = wx.NullColour, wx.NullColour

        if complete and regex:

            regColor = subColor = wx.BLUE
            try:
                re.sub(regex, subs, '')
            except re.error as e:
                subColor = wx.RED
                try:
                    re.compile(regex)
                except re.error as e:
                    regColor = wx.RED
                else:
                    self.m_validFromRe = True
            else:
                self.m_validFromRe = True
                self.m_validPatterns = bool(subs)

        self.setTextColor(regexCtl, regColor)
        self.setTextColor(subsCtl,  subColor)

        if complete:
            self.populateFileList()
        else:
            self.m_applyBtn.Enabled = False


    def updateDiskFileList(self):
        """ Refresh our list of what's on disk. """

        if self.m_curPath:
            # Get me just the files please.
            for _, _, files in os.walk(self.m_curPath):
                break
        else:
            files = []

        files.sort()
        if files != self.m_diskNames:
            self.m_diskNames[:] = files
            self.m_newNames[:] = []

        self.populateFileList()


    def populateFileList(self):
        """
        Uses the list of files-on-disk and the regex patterns to build a
        list of what the directory will look like if we renamed the files.

        Because we're just-using a simple text list, we use symbols to show
        the user which filenames would change and whether they would produce
        any duplicates, substituting "*.*" with "\1.txt".
        """

        self.m_fileList.SetForegroundColour(wx.NullColour)

        # We'll need to track which file names are modified and which
        # file names duped.
        applicable, dupes = set(), set()

        if not self.m_validPatterns:
            # Regex's don't compile yet, just use the raw filename list.
            newNames = self.m_diskNames

        else:
            # Apply the substitution to the filename list to produce a
            # destination-name list, and identify whether the patterns
            # actually affect anything.
            #
            newNames, modifiedIndexes = [], []

            matcher = re.compile(self.m_reFromCtl.Value).subn
            subs    = self.m_reToCtl.Value

            for filename in self.m_diskNames:
                # Perform the sub
                (filename, numChanges) = matcher(subs, filename)

                # Was there a modification?
                if numChanges:
                    # Record the affected name.
                    applicable.add(filename)
                    if filename in newNames:
                        dupes.add(filename)

                # Add to the primary list
                newNames.append(filename)

        # Does this produce a different list than we already had? If so,
        # clear the file list and replace it with the new one.
        #
        if newNames != self.m_newNames:

            self.m_fileList.Clear()

            # Figure out the longest name so we can create a cleanly-formatted
            # set of prefix/suffix characters for the modified/duped annotation.
            #
            maxLen = max(map(len, newNames))
            decorate = '{m} {fn:<{ml}} {m}'.format

            # Now build a list of display elements.
            for filename in newNames:
                mark = ' ' if filename not in applicable else '|'
                if filename in dupes:
                    mark = '*'
                self.m_fileList.Append(decorate(m=mark, fn=filename, ml=maxLen))

            # Keep the list.
            self.m_newNames[:] = newNames

        # Update the apply button, we only want it enabled when the user
        # has a valid set of patterns that affect any files and have no
        # dupes produced as a result.
        #
        self.m_applyBtn.Enabled = bool(applicable) and not dupes

        if dupes:
            # Emphasize the presence of dupes.
            self.m_fileList.SetForegroundColour(wx.RED)

        # Draw the list.
        self.m_fileList.Refresh()


    def onDirectorySelectionChanged(self, event):
        """ Handle the user changing directory. """

        newPath = self.m_directoryCtl.Path
        if self.m_curPath == newPath:
            return

        self.m_applyBtn.Disable()
        self.m_directoryCtl.ExpandPath(newPath)

        # Clear the directory list.
        self.m_fileList.Clear()

        self.m_curPath = newPath

        self.updateDiskFileList()


    def onApply(self, event):
        """ User has clicked the Apply button."""

        # Rename all of the files based on the substitution.
        for (old, new) in zip(self.m_diskNames, self.m_newNames):
            if old != new:
                old = os.path.join(self.m_curPath, old)
                new = os.path.join(self.m_curPath, new)
                try:
                    os.rename(old, new)
                except OSError:
                    pass

        # Now we out the lists so that what the user sees after this
        # reflects what's on disk.
        self.m_diskNames[:] = []
        self.m_newNames[:] = []

        # Update.
        self.updateDiskFileList()


    def onHitEnterInFrom(self, event):
        """ When the user hits 'enter' in the 'from' field. """

        self.validateRegexFields(complete=True)
        if self.m_validFromRe:
            self.m_reToCtl.SetFocus()


    def onHitEnterInTo(self, event):
        """ When the user hits 'enter' in the substitution field. """

        self.validateRegexFields(complete=True)
        if self.m_validPatterns:
            self.m_fileList.SetFocus()


    def onTextChange(self, event):
        """ When the user modifies the content of either regex field. """

        self.validateRegexFields(complete=False)
        event.Skip()




app = App()
ren = ReNamerFrame(None)
ren.Show()
app.MainLoop()
