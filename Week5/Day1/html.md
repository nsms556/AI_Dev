# [Week5 - Day1] 부록 html 메모

## 표
  - \<table>\</table>
  - \<th>\</th>
    - table head
    - 표의 제목을 표시하는 역할
  - \<tr>\</tr>
    - table row
    - 표의 가로줄을 만드는 역할
  - \<td>\</td>
    - table data
    - 표의 셀을 만드는 역할
  - colspan, rowspan
    - 셀 합치기

  - example
    ``` html
    <table>
        <thead>
            <tr>
                <th></th>
                <th>col1</th>
                <th>col2</th>
            </tr>
        </thead>
        
        <tbody>
            <tr>
                <th>row1</th>
                <td>body1</td>
                <td>body2</td>
            </tr>
            <tr>
                <th>row2</th>
                <td>body1</td>
                <td>body2</td>
            </tr>
        </tbody>
    </table>
    ```
  - <table>
      <thead>
          <tr>
              <th></th>
              <th>col1</th>
              <th>col2</th>
          </tr>
      </thead>
      
      <tbody>
          <tr>
              <th>row1</th>
              <td>body1</td>
              <td>body2</td>
          </tr>
          <tr>
              <th>row2</th>
              <td>body1</td>
              <td>body2</td>
          </tr>
      </tbody>
    </table>