# KATINUO-Data-Preprocessing

## usage
```
python katino-data-preprocessing.py FILENAME MIN_LENGTH
```
| Parameter | meaning | e.g. |
| -------- | -------- | -------- |
| FILENAME | 處理檔案名稱 | "katino_data.csv" |
| MIN_LENGTH |  Title 所需的最小長度 若太短則刪除| 10|
執行完後即會輸出 ==FILENAME_adjust.npy==

## example
```
python katino-data-preprocessing.py "katino_data.csv" 10
```
執行完後即會輸出 ==katino_data_adjust.npy==

## what this program do
1. 刪除 時事 政治的資料
1. 去除前後的括號(含有文字)
1. 將 \u300 轉換成空白 
1. 將字數小於 MIN_LENGTH 的title 刪除
