# from copy import deepcopy
#
#
# def dfs(ans, graph, trace, start):
#     trace = deepcopy(trace)  # 深拷贝，对不同起点，走过的路径不同
#
#     # 如果下一个点在trace中，则返回环
#     if start in trace:
#         index = trace.index(start)
#         tmp = [str(i) for i in trace[index:]]
#         ans.add(str(' '.join(tmp)))
#         return
#
#     trace.append(start)
#
#     for i in graph[start]:
#         dfs(ans, graph, trace, i)
#
#
# def algorithm():
#     # 用集合去除重复路径
#     ans = set()
#
#     graph = [[1], [2, 3], [0, 3, 4], [0], [2]]  # 包含大小环test图
#
#     dfs(ans, graph, [], 0)
#
#     return ans
#
# print(algorithm())

a = set([1, 2])
b = set([2, 1])

print(len(a - b))
