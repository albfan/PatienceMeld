import sys

__author__ = 'albfan'

### Multitree class

class MTree():

    def __init__(self, name):
        self.name = name
        self.childs = []

    def getName(self):
        return self.name

    def getChilds(self):
        return self.childs

    def addChild(self, node):
        self.childs.append(node)
        self.childs.sort()

    def hasChild(self, node):
        result = False
        for item in self.childs:
            if item.getName() == node:
                result = True
                break
        return result

    def countChilds(self):
        return len(self.childs)

    def getChild(self, node):
        for item in self.childs:
            if item.getName() == node:
                return item
        return None

    def printItem(self, space=""):
        if self.countChilds():
            hijos = ""
            for item in self.childs:
                hijos += item.getName() + ", "
            hijos = hijos[:-2]
            name = space + self.name + ": "
            print name + hijos
            space = ""
            for i in range(len(name)):
                space += " "
            
            for item in self.childs:
                item.printItem(space)
        else:
            print space + self.name

    def contains_path(self, path):
        resultado = False
        path_items = path.split("/")
        tree = self;
        for pit in path_items:
            resultado = tree.countChilds()
            if resultado:
                resultado = tree.hasChild(pit)
                if resultado:
                    tree = tree.getChild(pit)
                else:
                    break
            else:
                break
        return resultado

def print_rsync_file(filename):

    """Prints the file"""
    rsync_file = open(filename, "r")
    print rsync_file.read()
    rsync_file.close()

def parse_rsync_file(filename):

    """Build a directory tree from list in filename"""
    rsync_file = open(filename, "r")
    rsync_paths = rsync_file.readlines()
    rsync_file.close()
    root = MTree("root")
    tree = root
    for file in rsync_paths:
        path_items = file.split("/")
        tree = root
        for item in path_items:
            item = item.replace("\n","")
            if not len(item):
                continue
            if tree.hasChild(item):
                tree = tree.getChild(item)
            else:
                item_tree = MTree(item)
                tree.addChild(item_tree)
                tree = item_tree
    return root

def main():
    print_rsync_file(sys.argv[1])
    tree = parse_rsync_file(sys.argv[1])
    tree.printItem()

    def treecontains(tree, path):

        """test utillery"""
        if tree.contains_path(path):
           print path + " EXISTS"
        else:
            print path + " NOT EXISTS"

    treecontains(tree, "foo")
    treecontains(tree, "bar/bazz")

if __name__ == "__main__":
    main()

