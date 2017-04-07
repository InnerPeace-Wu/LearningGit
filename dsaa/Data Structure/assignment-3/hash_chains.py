# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class listnode:

    def __init__(self, value):
        self.val = value
        self.next = None


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = []
        self.items = []
        for  i in range(self.bucket_count):
            self.items.append(listnode(i))

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def chain_write(self, chain):
        chain = chain.next
        result = ''
        while chain != None:
            result += (str(chain.val) + ' ')
            chain = chain.next
        print(result)

    @staticmethod
    def _find_query(chain, string):
        chain = chain.next
        while chain != None:
            if chain.val == string: return True
            chain = chain.next
        return False

    def _del_query(self, index, string):
        chain = self.items[index].next
        dump_head = listnode(0)
        temp = dump_head
        while chain != None:
            if chain.val == string:
                temp.next = chain.next
                self.items[index].next = dump_head.next
                break
            temp.next = chain
            temp = temp.next
            chain = chain.next

    def read_query(self):
        return Query(input().split())

    def processing(self, query):
        #print(self.items)
        if query.type == 'check':
            if self.items[query.ind].next == None: print('\n')
            else: self.chain_write(self.items[query.ind])
        else:
            index = self._hash_func(query.s)
            if query.type == 'find' :
                self.write_search_result(self._find_query(self.items[index], query.s))
            elif query.type == 'add' and self._find_query(self.items[index], query.s) == False:

                temp_head = self.items[index].next
                new_node = listnode(query.s)
                new_node.next = temp_head
                self.items[index].next = new_node
                #self.chain_write(self.items[index])
            elif query.type == 'del':
                self._del_query(index, query.s)
                #temp_head = self.items[index].next.next
                #self.items[index].next = temp_head

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(cur for cur in reversed(self.elems)
                        if self._hash_func(cur) == query.ind)
        else:
            try:
                ind = self.elems.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    self.elems.append(query.s)
            else:
                if ind != -1:
                    self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            #self.process_query(self.read_query())
            self.processing(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
