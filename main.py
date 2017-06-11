import csv
import plotly.plotly as py
import plotly.graph_objs as go

with open('/Users/admin/Downloads/Hamilton1.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    included_cols = [24]
    content = list()
    label = []
    labels = []
    value = []
    values = []
    numberofrecords = 0
    for row in reader:
        numberofrecords = numberofrecords + 1
        rowcontent = list(row[i] for i in included_cols)
        if not (rowcontent in content):
            content = content + rowcontent
    
    contentset = set(content)
    contentset = list(contentset)
    
    for row in contentset:
        
        label = [row]
        labels = keys + key
        
        k = content.count(row)
        value = [k]
        values = values + value
    
    print (labels)   
    print (values)
    print (numberofrecords)
        
    
trace = go.Pie(labels=labels, values=values)

py.iplot([trace], filename='basic_pie_chart')
