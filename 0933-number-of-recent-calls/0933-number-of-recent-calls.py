class RecentCounter(object):

    def __init__(self):
        self.req=[]

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.req.append(t)
        while self.req[0]<t-3000:
            self.req.pop(0)
        return len(self.req)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)