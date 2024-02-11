class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#root - корень дерева, по которому производится поиск путей
#target_sum - сумма
def find_paths(root, target_sum):
    #node - текущий узел дерева
    #current_sum - текущая сумма на пути от корня до node
    #path - список, содержащий значения узлов на пути от корня до node
    def dfs(node, current_sum, path):
        if not node:
            return
        current_sum += node.val
        path.append(node.val)
        if not node.left and not node.right and current_sum == target_sum:
            print("->".join(map(str, path)))
        dfs(node.left, current_sum, path[:])
        dfs(node.right, current_sum, path[:])
    if not root:
        return
    dfs(root, 0, [])

# Функция для создания дерева из введенного списка узлов
def create_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue:
        node = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# Ввод списка узлов от корня до последнего уровня
nodes_input = input("Введите список узлов от корня до последнего уровня (через запятую, для пропущенных узлов введите None) пример: 1,3,None,5: ").split(",")
nodes = [int(node) if node != "None" else None for node in nodes_input]

# Создание дерева
root = create_tree(nodes)

# Ввод целевой суммы
target_sum = int(input("Введите целевую сумму: "))

# Поиск путей
find_paths(root, target_sum)
