# for tc in range(1, int(input())+1):
#     tw_n = list(map(int, input()))
#     th_n = list(map(int, input()))
#     tw_l = len(tw_n)
#     th_l = len(th_n)
#
#     tw_lst = []
#     th_lst = []
#
#     tw_ret = []
#     th_ret = []
#
#     for i in range(tw_l):
#         if tw_n[i] == 0:
#             tw_n[i] = 1
#             tw_lst.append(tw_n)
#             tw_n[i] = 0
#         else:
#             tw_n[i] = 0
#             tw_lst.append(tw_n)
#             tw_n[i] = 1
#
#     for i in range(th_l):
#         if th_n[i] == 1:
#             th_n[i] = 2
#             th_lst.append(th_n)
#             th_n[i] = 1
#         else:
#             th_n[i] = 1
#             th_lst.append(th_n)
#             th_n[i] = 2
#
#     for j in range(tw_l):
#         twn = 0
#         s = tw_l -1
#         for k in range(tw_l):
#             if tw_lst[j][j] == 1:
#                 twn += 2**s
#                 s -= 1
#             else:
#                 twn += 1
#                 s -= 1
#         tw_ret.append(twn)
#
#     for j in range(th_l):
#         thn = 0
#         s = th_l -1
#         for k in range(th_l):
#             thn =
#         tw_ret.append(thn)
#
