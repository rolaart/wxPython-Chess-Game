import wx
import wx.grid
import os
from board import Board

defaultBoard = Board(8,8)

class Chess(wx.Frame):
    def __init__(self,*args,**kws):
        super(Chess,self).__init__(*args, **kws)
        self.InitUI()

    def OnClose(self,e):
        self.Close(True)

    def StartGame(self, e):
        self.chessBoard = defaultBoard
        for i in range(8):
            for j in range(8):
                self.grid.SetCellValue(i,j,'')
                if self.chessBoard.is_piece(i,j):
                    self.grid.SetCellValue(i,j,self.chessBoard.get_img(i,j))

    def Move(self,e):
        if self.inHand != '' and self.grid.GetCellValue(e.Row, e.Col) != '':
            self.remarks.SetValue('There\'s a figure there!')
        elif self.inHand != '':
            self.grid.SetCellValue(e.Row, e.Col, self.inHand)
            self.inHand = ''
            self.remarks.SetValue('')
            self.pickedUp = None
        else:
            self.inHand = self.grid.GetCellValue(e.Row, e.Col)
            self.pickedUp = self.chessBoard.board[e.Row][e.Col]
            self.grid.SetCellValue(e.Row, e.Col, '')

    def InitUI(self):
        pnl = wx.Panel(self)
        self.grid = wx.grid.Grid(pnl)
        self.grid.CreateGrid(8,8,False)
        self.grid.SetSize(565,515)
        self.grid.EnableDragColSize(False)
        self.grid.EnableDragRowSize(False)
        self.grid.EnableEditing(False)
        for i in range(8):
            self.grid.SetRowSize(i,60)
            self.grid.SetColSize(i,60)
        for i in range(8):
            for j in range(8):
                if i%2 == 0:
                    if j%2 != 0:
                        self.grid.SetCellBackgroundColour(i,j,wx.BLACK)
                        self.grid.SetCellTextColour(i,j,wx.WHITE)
                else:
                    if j%2 == 0:
                        self.grid.SetCellBackgroundColour(i,j,wx.BLACK)
                        self.grid.SetCellTextColour(i,j,wx.WHITE)
        self.inHand = ''
        self.pickedUp = None
        startbtn = wx.Button(pnl, label = 'New Game', pos = (10,525))
        startbtn.Bind(wx.EVT_BUTTON, self.StartGame)
        closebtn = wx.Button(pnl, label = 'Close', pos = (100,525))
        closebtn.Bind(wx.EVT_BUTTON, self.OnClose)
        remarksBox = wx.StaticText(pnl, label = 'Remarks:', pos = (570,40))
        self.remarks = wx.TextCtrl(pnl, style = wx.TE_MULTILINE | wx.TE_WORDWRAP, pos = (570,60), size = (150,250))
        self.grid.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.Move)
        self.remarks.SetEditable(False)
        self.SetSize((750,650))
        self.SetTitle('wxChess')
        self.Centre()
        self.Show(True)


def main():
    game = wx.App()
    Chess(None)
    game.MainLoop()

if __name__ == '__main__':
    main()
