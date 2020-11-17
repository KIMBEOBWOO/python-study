# 게시물의 총 건수(m)	페이지당 보여줄 게시물 수(n)	총 페이지 수
# 5	    10	    1
# 15	10	    2
# 25	10	    3
# 30	10	    3

def getTotalPage(m, n):
    mantisa, fraction = divmod(m, n)
    return mantisa + (fraction > 0 and 1 or 0)


dummy = [(5, 10), (15, 10), (25, 10), (30, 10)]
for i, (m, n) in enumerate(dummy):
    print(i, "total page = %x" % getTotalPage(m, n))
