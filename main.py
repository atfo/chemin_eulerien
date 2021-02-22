import dir
import undir

if __name__ == '__main__':
    adju = [ [1,2,3],
        [3,3,0,2],
        [1,0,3],
        [1,1,0,2] ]
    adj1 = [[1, 2],
           [3, 3],
           [1, 0],
           [0, 2]]
    adj2 = [ [], [0], [3], [1] ]
    print(undir.euler(adju))
    print(dir.euler(adj2))

