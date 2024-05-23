for i in range(0,20):
    if not i % 3 or not i % 5:
        continue
    print(i)

    #for x in range(21):
        # if x % 3 == 0 or x % 5 == 0:
    #     continue
    # print(x)

# without continue
# for x in range(21):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)
#