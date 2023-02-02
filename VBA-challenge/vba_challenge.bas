Option Explicit
Sub ticker_challenge()
'declare variable types here
    Dim _
        a As Application, wb As Workbooks, this_wb As Workbook, row_last As Long, rng As Range, _
        i As Long, sht As Worksheet, ticker_dict As Object, closing_val As Double, _
        k As String, volume As Double, open_val As Double, pct_change As Double, change As Double, rng_cell As Range, _
        tick_rng As Range, pct_rng As Range, volume_rng As Range, shts As Long, x As Long

'Set constant variables
    Set a = Application
    Set wb = Workbooks
    Set this_wb = ThisWorkbook
    shts = this_wb.Sheets.Count
a.ScreenUpdating = False
'loop sheets
    For i = 1 To shts
        Set sht = this_wb.Sheets(i)
        'create ticker column.
        With sht
            .Range("I1").Value = "Ticker"
            .Range("J1").Value = "Yearly Change"
            .Range("K1").Value = "Percent Change"
            .Range("L1").Value = "Total Stock Volume"
            
            Set ticker_dict = CreateObject("Scripting.Dictionary")

            'find last row
            row_last = .Range("A:A").SpecialCells(xlCellTypeLastCell).Row
            
            'set range for, For Each Loop and fill ticker column
            
            Set rng = .Range("A2:A" & row_last)
            x = 2
            For Each rng_cell In rng
                'Capture k(ey), capture/update closing value
                k = rng_cell.Value
                closing_val = rng_cell.Offset(0, 5).Value
                
                If Not ticker_dict.Exists(k) Then
                    'ticker not added yet, start
                    ticker_dict.Add Key:=k, Item:=closing_val
                    open_val = rng_cell.Offset(0, 2).Value
                    'volume = rng_cell.Offset(0, 6).Value
                Else
                    'update item closing value, and keep running sum of the ticker
                    .Range("I" & x).Value = k
                    ticker_dict(k) = closing_val
                    'volume = rng_cell.Offset(0, 6).Value + volume
                    If rng_cell.Offset(1, 0).Value <> k Then
                        change = Round(closing_val - open_val, 2)
                        pct_change = Round((closing_val - open_val) / open_val, 4)
                        .Range("J" & x).Value = change
                        .Range("K" & x).Value = pct_change
                        volume = a.WorksheetFunction.SumIf(rng, k, .Range("G2:G" & row_last))
                        .Range("L" & x).Value = volume
                        .Range("K" & x).NumberFormat = "0.00%"
                        .Range("L" & x).NumberFormat = "#,##0"
                        x = x + 1
                        volume = 0
                    End If
                End If
            
            Next rng_cell
                            
             'Create table for following statistics
            .Range("O2").Value = "Greatest % Increase"
            .Range("O3").Value = "Greatest % Decrease"
            .Range("O4").Value = "Greatest Total Volume"
            .Range("P1").Value = "Ticker"
            .Range("Q1").Value = "Value"
            
            'Find Values
            row_last = .Range("K:K").SpecialCells(xlCellTypeLastCell).Row
            
            Set rng = .Range("J2:J" & row_last)
            Set pct_rng = .Range("K2:K" & row_last)
            Set tick_rng = .Range("I2:I" & row_last)
            Set volume_rng = .Range("L2:L" & row_last)

            'add "conditional" formatting to yearly change col
            for each rng_cell in rng
                if rng_cell.value >= 0 Then
                    rng_cell.Interior.Color = vbGreen
                Else
                    rng_cell.Interior.Color = vbRed
                End If
            next rng_cell

            'add "conditional" formatting to percent change col
            for each rng_cell in pct_rng
                if rng_cell.value >= 0 Then
                    rng_cell.Interior.Color = vbGreen
                Else
                    rng_cell.Interior.Color = vbRed
                End If
            next rng_cell
            

            'find greatest increase
            .Range("Q2").Value = a.WorksheetFunction.Max(pct_rng)
            .Range("Q2").NumberFormat = "0.00%"
            .Range("P2").Value = a.WorksheetFunction.XLookup(.Range("Q2").Value, pct_rng, tick_rng, "Error", 0, 1)
            
            'find greatest decrease
            .Range("Q3").Value = a.WorksheetFunction.Min(pct_rng)
            .Range("Q3").NumberFormat = "0.00%"
            .Range("P3").Value = a.WorksheetFunction.XLookup(.Range("Q3").Value, pct_rng, tick_rng, "Error", 0, 1)
                            
            'find greatest volume
            .Range("Q4").Value = a.WorksheetFunction.Max(volume_rng)
            .Range("Q4").NumberFormat = "#,##0"
            .Range("P4").Value = a.WorksheetFunction.XLookup(.Range("Q4").Value, volume_rng, tick_rng, "Error", 0, 1)

            'fix visual appearance of data                
            .Columns.AutoFit
            'clear ticker memory for next worksheet
            ticker_dict.RemoveAll
        End With
    Next i
    a.ScreenUpdating = True
    'communicate with user
    MsgBox ("SUCCESS")
End Sub

