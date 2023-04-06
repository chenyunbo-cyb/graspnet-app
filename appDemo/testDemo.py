import sys
print(sys.path)
sys.path.append('E:\graspnet\graspnet-baseline')
sys.path.append('E:\graspnet\graspnet-baseline\appDemo')
# sys.path.append('E:\graspnet\graspnet-baseline')

import demo

if __name__=='__main__':
    data_dir = 'doc/example_data'
    demo.demo(data_dir)