import sys

class Vertex:

    __slots__ = "left","right"

    def __init__(self,L,R):
        self.left=L
        self.right=R

def findPath(Matrix,myDic,row,column,w,h):
    """
    just to prevent the same key in the dictionary,so the corresponding value is covered
    """
    if str(row)+","+str(column) in myDic.keys():
        return
    myArray = []
    """
    put every coordinate that we can reach in the myArray
    注意矩阵和本题的坐标逻辑相反
    """

    for m in range(row, h):
        if Matrix[column][m] == "*":
            myArray.append(str(m - 1)+ "," +str(column) )
            break
        if m == h - 1:
            myArray.append(str(h - 1) + "," + str(column))
    print(myArray)
    for n in range(row, -1, -1):
        if Matrix[column][n] == "*":
            myArray.append(str(n + 1) + "," + str(column))
            break
        if n == 0:
            myArray.append( str(n) + "," +str(column))
    print(myArray)
    for p in range(column, w):
        if Matrix[p][row] == "*":
            myArray.append( str(row) + "," +str(p - 1))
            break
        if p == w - 1:
            myArray.append(str(row) + "," +str(p) )
    print(myArray)
    for q in range(column, -1, -1):
        if Matrix[q][row] == "*":
            myArray.append(str(row) + "," + str(q + 1))
            break
        if q == 0:
            myArray.append(str(row) + "," +str(q) )
    print(myArray)
    """
    add the index of the repeated element in the myArray
    """
    crr=[]
    for index in range(0,len(myArray)):
        if myArray[index] == str(row) + "," + str(column):
            crr.append(index)
    """
    construct a new array brr from myArray that does not contain the same element twice
    """
    if len(crr)==1:
        brr = []
        for i in range(0, len(myArray)):
            if i == crr[0]:
                pass
            else:
                brr.append(myArray[i])
    elif len(crr)==2:
        brr = []
        for j in range(0, len(myArray)):
            if j == crr[0] :
                pass
            elif j==crr[1]:
                pass
            else:
                brr.append(myArray[j])
    else:
        brr=myArray
    print(brr)
    """
    use the data structure dictionary to store coordinate and its neighbors
    """
    myDic[str(row) + "," + str(column)] = brr
    print(myDic)
    """
    use the concept of recursive to creat all the coordinates and their neighbors
    """
    arr=myDic[str(row) + "," + str(column)]
    for x in range(0,len(arr)):
        aString=arr[x]
        arow=int(aString[0])
        acolumn=int(aString[2])
        # print(str(arow)+","+str(acolumn))
        findPath(Matrix,myDic,arow,acolumn,w,h)
    """
    the dictionary contains all the path which starting point may pass
    """
    return myDic


def BFS(graph,s):
    """
    the algorithm of BFS to create parent dictionary and to find the path
    """
    queue=[]
    queue.append(s)
    seen=set()
    seen.add(s)
    parent={s:None}
    while len(queue)>0:
        vertex=queue.pop(0)
        nodes=graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w]=vertex
        # print(vertex)
    return parent


def test():
    d1=[]
    d2=[]
    d3=[]
    d4=[]
    d5=[]
    d6=[]
    d7=[]
    d8=[]
    i = 0
    j=0
    """
    to give the input txt file name from the command line
    """
    filename = sys.argv[1] + '.txt'
    with open(filename) as f:
        f.readline()
        for line in f:
            """
            use the data structure of two dimensional array to store the input data
            """
            if j==0:
                arr=line.split()
                """
                the width and height of the given input txt
                """
                h=int(arr[0])
                w=int(arr[1])
                Matrix = [[0 for x in range(w)] for y in range(h)]
                print(Matrix)
                j+=1
            else:
                brr=line.split()
                for index in range(0,len(brr)):
                    Matrix[i][index]=brr[index]
                i+=1
    print(Matrix)
    """
    give the starting coordinate of the ice maze
    the x coordinate and y coordinate
    """
    """
    return the dictionary from the method findPath 
    """
    for xcoord in range(0,w):
        for ycoord in range(0,h):
            if Matrix[xcoord][ycoord]!="*":
                row=ycoord
                column=xcoord
                print(str(row)+","+str(column))
                myDic = {}
                aDic=findPath(Matrix,myDic,row,column,w,h)
                print("Gooooooooooooooooooooooooooooooooooooooooooogle")
                for key in aDic.keys():
                    if key==str(sys.argv[2])+","+sys.argv[3]:
                        pass
                    else:
                        parent=BFS(aDic, key)
                        print(parent)
                        """
                        finally,finding all the distances to the escape exit and
                        which coordinates can have this distance
                        """
                        if str(sys.argv[2])+","+sys.argv[3] in parent.keys():
                            parameter = parent[str(sys.argv[2])+","+sys.argv[3]]
                            counter = 0
                            err=[]
                            err.append(str(sys.argv[2])+","+sys.argv[3])
                            while parameter is not None:
                                err.append(parameter)
                                parameter=parent[parameter]
                                counter+=1
                            if err[-1]!=str(row)+","+str(column):
                                print("can not reach")
                            else:
                                print(err)
                                print(counter)
                                if counter==1:
                                    d1.append("("+str(row)+","+str(column)+")")
                                elif counter == 2:
                                    d2.append("(" + str(row) + "," + str(column) + ")")
                                elif counter==3:
                                    d3.append("("+str(row)+","+str(column)+")")
                                elif counter==4:
                                    d4.append("("+str(row)+","+str(column)+")")
                                elif counter==5:
                                    d5.append("("+str(row)+","+str(column)+")")
                                elif counter==6:
                                    d6.append("("+str(row)+","+str(column)+")")
                                elif counter==7:
                                    d7.append("("+str(row)+","+str(column)+")")
                                elif counter==8:
                                    d8.append("("+str(row)+","+str(column)+")")
                        else:
                            print("can not reach")
    print("1:",end="")
    d1.append(str(sys.argv[2])+","+sys.argv[3])
    print(d1)
    print("2:", end="")
    print(d2)
    print("3:", end="")
    print(d3)
    print("4:", end="")
    print(d4)
    print("5:", end="")
    print(d5)
    print("6:", end="")
    print(d6)
    print("7:", end="")
    print(d7)
    print("8:", end="")
    print(d8)





if __name__ == '__main__':
    test()