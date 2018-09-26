
global Headers
Headers = {}

def la():

    for i in range(5):
        print('1', Headers)
        Headers['q']= i
        fo()
def fo():
    for j in range(10):
        print('fo',Headers)

if __name__ == '__main__':
    print('3',Headers)
    la()
    print('2',Headers)