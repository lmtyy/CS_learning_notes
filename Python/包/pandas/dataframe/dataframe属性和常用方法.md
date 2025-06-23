### **DataFrame 的属性**

1. **结构相关属性**
   - `df.shape`  
     返回 DataFrame 的形状 (行数, 列数)。
   - `df.size`  
     返回 DataFrame 的元素总个数。
   - `df.ndim`  
     返回 DataFrame 的维度，通常为 2。

2. **数据相关属性**
   - `df.dtypes`  
     返回每列的数据类型。
   - `df.columns`  
     返回列名的索引对象。
   - `df.index`  
     返回行索引。
   - `df.values`  
     返回 DataFrame 的值，以 NumPy 数组形式表示。
   - `df.empty`  
     如果 DataFrame 为空，返回 `True`。

3. **信息相关属性**
   - `df.info()`  
     输出 DataFrame 的结构和数据类型等详细信息。
   - `df.describe()`  
     对数值列进行统计汇总（均值、标准差、最小值、四分位数等）。

4. **布尔属性**
   - `df.isna()` 或 `df.isnull()`  
     检查每个元素是否为空值（NaN），返回布尔值 DataFrame。
   - `df.notna()` 或 `df.notnull()`  
     检查每个元素是否不是空值。

---

### **DataFrame 的常用方法**

#### **1. 数据查看与选取**
- `df.head(n)`  
  返回前 n 行，默认是 5 行。
- `df.tail(n)`  
  返回后 n 行，默认是 5 行。
- `df.sample(n)`  
  随机返回 n 行数据。
- `df.loc[]`  
  按标签（索引、列名）选取数据。
- `df.iloc[]`  
  按位置（行号、列号）选取数据。

#### **2. 数据修改**
- `df.rename(columns={'old': 'new'})`  
  修改列名。
- `df.set_index('column')`  
  设置某列为索引。
- `df.reset_index()`  
  重置索引为默认数值索引。
- `df.drop(columns='column', inplace=True)`  
  删除指定列。

#### **3. 数据运算**
- `df.sum(axis=0)`  
  对列（行方向）求和，`axis=1` 对行（列方向）求和。
- `df.mean()`  
  计算均值。
- `df.median()`  
  计算中位数。
- `df.min()`/`df.max()`  
  返回最小值/最大值。
- `df.corr()`  
  返回列与列之间的相关性系数矩阵。
- `df.count()`  
  返回每列非空值的数量。

#### **4. 数据筛选与分组**
- `df[df['column'] > value]`  
  按条件筛选数据。
- `df.groupby('column')`  
  按某列分组。
- `df.groupby('column').agg({'col1': 'mean', 'col2': 'sum'})`  
  对分组后的列进行聚合操作。

#### **5. 数据处理**
- `df.dropna()`  
  删除含有缺失值的行。
- `df.fillna(value)`  
  填充缺失值。
- `df.replace({'old_value': 'new_value'})`  
  替换指定值。
- `df.duplicated()`  
  检查是否有重复行。
- `df.drop_duplicates()`  
  删除重复行。

#### **6. 数据排序**
- `df.sort_values(by='column', ascending=True)`  
  按某列排序，默认升序。
- `df.sort_index(ascending=False)`  
  按索引排序。

#### **7. 数据合并与连接**
- `pd.concat([df1, df2], axis=0)`  
  沿行方向拼接。
- `pd.merge(df1, df2, on='column')`  
  根据某列进行合并。

#### **8. 数据转换**
- `df.astype({'column': 'int'})`  
  转换列的数据类型。
- `df.apply(func, axis=0)`  
  按列或行应用自定义函数。
- `df.applymap(func)`  
  对所有元素应用函数。

#### **9. 数据导入与导出**
- `pd.read_csv('file.csv')`  
  从 CSV 文件读取数据。
- `df.to_csv('file.csv', index=False)`  
  将 DataFrame 保存为 CSV 文件。
- `pd.read_excel('file.xlsx')`  
  从 Excel 文件读取数据。
- `df.to_excel('file.xlsx', index=False)`  
  将 DataFrame 保存为 Excel 文件。

#### **10. 数据统计**
- `df.nunique()`  
  返回每列的唯一值数量。
- `df.value_counts()`  
  返回某列中每个值出现的次数。

如果需要详细示例，欢迎进一步探讨！