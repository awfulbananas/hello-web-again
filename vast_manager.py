import subprocess
from subprocess import PIPE

searchCall = ['vastai', 'search offers', 'cpu_cores>=10 gpu_total_ram>=8 reliability>=0.95 dph<2']

def find_instance() -> str:
    searchOut = subprocess.run(searchCall, check=True, stdout=PIPE, text=True).stdout
    rows = searchOut.split('\n')
    if(len(rows) < 2):
        return "Failed"
    table = [row.split() for row in rows]
    tableHeader = table[0]
    tableData = [table[i] for i in range(1, len(table))]
    costInd = tableHeader.index("$/hr")
    print("     unsorted:")
    print(tableHeader)
    print(tableData)
    def data_sorter(row):
        print("cost ind: " + str(costInd))
        return row[costInd]
    
    tableData.sort(key=data_sorter)
    print("     sorted:")
    print(tableHeader)
    print(tableData)
    return ""