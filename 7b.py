import re

WEIGHT_NOT_FOUND = 0
COR_WEIGHT_FOUND = 1
MORE_DATA_NEEDED = 2

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

    '''def findImbalance(self):
        temp = None
        total = 0
        prepreturn = (False,0)
        nextpass = (False,0,0)
        for i, c in enumerate(self.children):
            r = c.findImbalance()
            total += r[1]
            if r[0]:
                return r
            elif len(r) > 2 or nextpass[0]:
                nextpass = r
                if i > 0:
                    if c.weight + nextpass[1] == temp:
                        return (True, nextpass[1])
                    else:
                        return (True, nextpass[2])
            if temp == None:
                temp = r[1]
            elif temp != r[1]:
                if i != 1 and not prepreturn[0]:
                    return (True, temp)
                elif prepreturn[0]:
                    return prepreturn
                else:
                    prepreturn = (True, r[1])
        if nextpass[0]:
            return (True, nextpass[1] + self.weight, nextpass[2] + self.weight)
        if not prepreturn[0]:
            return (False, self.weight + total)
        else:
            return (False, prepreturn[1], temp)
        if len(self.children) == 0:
            return (False, self.weight)'''

    def findImbalance(self):
        programweights = []
        moredata = (False, (0,))
        for i, c in enumerate(self.children):
            r = c.findImbalance()
            if r[0] == WEIGHT_NOT_FOUND:
                programweights.append(r)
            elif r[0] == COR_WEIGHT_FOUND:
                return r
            elif r[0] == MORE_DATA_NEEDED:
                moredata = (True, r)
                programweights.append(r)
        #print(programweights)
        if len(programweights) == 1:
            r = programweights[0]
            if moredata[0]:
                return (MORE_DATA_NEEDED, self.weight + r[1], r[2], r[3], r[4], r[5])
            return (WEIGHT_NOT_FOUND, self.weight, r[1] + r[2])
        else:
            if moredata[0]:
                for p in programweights:
                    #print(p)
                    #print(moredata[1])
                    if p != moredata[1]:
                        if p[1] + p[2] == moredata[1][1] + moredata[1][2] + moredata[1][3]:
                            return (COR_WEIGHT_FOUND, moredata[1][2])
                        else:
                            return (COR_WEIGHT_FOUND, moredata[1][4])
            else:
                temp = 0
                neat = 0
                total = 0
                possiblemoredata = (False, (0,))
                for i, p in enumerate(programweights):
                    total += p[1]+p[2]
                    if i == 0:
                        temp = p[1]+p[2]
                        neat = p[2]
                    else:
                        if p[1] + p[2] != temp:
                            if i > 1 and not possiblemoredata[0]:
                                return (COR_WEIGHT_FOUND, temp - p[2])
                            elif possiblemoredata[0]:
                                return (COR_WEIGHT_FOUND, (p[1] + p[2]) - neat)
                            else:
                                possiblemoredata = (True, p)
                        elif possiblemoredata[0]:
                            return (COR_WEIGHT_FOUND, temp - possiblemoredata[1][2])
                if possiblemoredata[0]:
                    return (MORE_DATA_NEEDED, self.weight, possiblemoredata[1][1], possiblemoredata[1][2], temp - neat, neat, self.name)
                else:
                    return (WEIGHT_NOT_FOUND, self.weight, total, self.name)


def solution(input):
    numre = re.compile("[0-9]+")
    namere = re.compile("[a-z]+")
    heads = []
    names1 = set()
    names2 = set()
    for l in input:
        wh = l.split()
        nm = wh[0]
        if nm in names1:
            print(nm)
            print('ohno repeated')
        names1.add(nm)
        wt = numre.findall(wh[1])[0]
        tr = Tree(nm)
        tr.weight = int(wt)
        if len(wh) > 2:
            nms = namere.findall(l)[1:]
            for n in nms:
                if n in names2:
                    print(n)
                    print('ohno two refs')
                names2.add(n)
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
    print(heads[0].findImbalance()[1])


if __name__ == "__main__":
    import sys
    tfile = open(sys.argv[1], 'r')
    solution(tfile.readlines())
    #solution(sys.argv[1])
