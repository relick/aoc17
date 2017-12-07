import re

class Tree:
    def __init__(self, nm):
        self.children = []
        self.weight = None
        self.name = nm

    def findName(self,name):
        for c in self.children:
            r = c.findName(name)
            if r != None:
                return r
        if self.name == name:
            return self
        else:
            return None

def solution(input):
    numre = re.compile("[0-9]+")
    namere = re.compile("[a-z]+")
    heads = []
    for l in input:
        wh = l.split()
        nm = wh[0]
        wt = numre.findall(wh[1])[0]
        tr = Tree(nm)
        tr.weight = wt
        if len(wh) > 2:
            nms = namere.findall(l)[1:]
            for n in nms:
                notfound = True
                for h in heads:
                    if h.name == n:
                        tr.children.append(h)
                        heads.remove(h)
                        notfound = False
                        break
                if notfound:
                    tr.children.append(Tree(n))
        notfound = True
        for h in heads:
            n = h.findName(nm)
            if n != None:
                n.children = tr.children
                n.weight = tr.weight
                notfound = False
                break
        if notfound:
            heads.append(tr)
    print(heads[0].name)


if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
