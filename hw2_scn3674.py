import timeit
import time
import matplotlib.pyplot as plt

class MySorted:
    def __init__(self, data = [], comp = 0, swap = 0):
            self.data = data
            self.comp = comp
            self.swap = swap
            self.bubble_time = 0
            self.merge_time = 0
    def __len__(self):
            return len(self.data)

    def bubble_sorted(self, input, key = None, reverse = False):
        # input: iterable of objects to sort
        # key: the function which the sorting based on
        # reverse: returning the sorted list in ascending oder if False, descending order if True.
        if key ==None:
            key= lambda x:x
        start_time = time.time()
        self.data = input
        input_key = list(map(key,input))
        mydict = dict(zip(input_key,input))
        l = len(input)
        self.comp = 0
        self.swap = 0
        if l == 0 or l == 1:
            print("Number of comparisons are: %s " % (self.comp))
            print("Number of swaps are: %s " % (self.swap))
            print("Timer measure is: %s " % ("{:.2e}".format(self.bubble_time)))
            return input
        if reverse==True:
            for i in range(l-1):
                for j in range(0, l-i-1):
                    self.comp += 1
                    if input_key[j] < input_key[j+1]:
                        input_key[j], input_key[j+1] = input_key[j+1], input_key[j]
                        self.swap += 1
        else:
            for i in range(l-1):
                for j in range(0, l-i-1):
                    self.comp += 1
                    if input_key[j] > input_key[j+1]:
                        input_key[j], input_key[j+1] = input_key[j+1], input_key[j]
                        self.swap += 1

        list0=input_key
        result = [mydict[key] for key in list0]
        print("Number of comparisons are: %s " % (self.comp))
        print("Number of swaps are: %s " % (self.swap))
        self.bubble_time = time.time() - start_time
        print("Timer measure is: %s " % ("{:.2e}".format(self.bubble_time)))
        return result


    def merge_sorted(self, input, key=lambda x:x, reverse = False):
        # input: iterable of objects to sort
        # key: the function which the sorting based on
        # reverse: returning the sorted list in ascending oder if False, descending order if True.
        start_time = time.time()
        self.data = input
        l = len(self)
        self.comp = 0
        self.swap = 0
        input_key = list(map(key,input))
        mydict = dict(zip(input_key,input))
        if l == 0 or l == 1:
            print("Number of comparisons are: %s " % (self.comp))
            print("Timer measure is: %s " % ("{:.2e}".format(self.merge_time)))
            return input
    
        def merge_sort(list0):
            if len(list0) > 1:
                mid = len(list0) // 2
                left_half = list0[:mid]
                right_half = list0[mid:]
                merge_sort(left_half)
                merge_sort(right_half)
                i= 0
                j= 0
                k= 0
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]: 
                        list0[k] = left_half[i] 
                        i=i+ 1
                        self.comp += 1
                    else:
                        list0[k] = right_half[j] 
                        j=j+ 1
                        self.comp += 1
                    k=k+ 1
                while i < len(left_half):
                    list0[k] = left_half[i] 
                    i=i+ 1
                    k=k+ 1
                while j < len(right_half): 
                    list0[k] = right_half[j] 
                    j=j+ 1
                    k=k+ 1

        list0 = input_key
        merge_sort(list0)
        if (reverse == False):
            result = [mydict[key] for key in list0]
        if (reverse == True):
            list0.reverse()
            result = [mydict[key] for key in list0]
        print("Number of comparisons are: %s " % (self.comp))
        self.merge_time = time.time() - start_time
        print("Timer measure is: %s " % ("{:.2e}".format(self.merge_time)))
        return result

 