from collections import defaultdict

class Graph:
    def __init__ (self, subjects):
        self.subjects = subjects
        self.graph = defaultdict(list)
    
    def add_edge(self, subject1, subject2):
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def graph_coloring(self):
        color_map={}
        available_colors = set(range(1, len(self.subjects)+1))
        for subject in self.subjects:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])

            available_colors = available_colors - used_colors

            if available_colors:
                color_map[subject] = min(available_colors)
            else:
                color_map[subject] = len(available_colors) + 1
                available_colors.add(color_map[subject])
        return color_map

    def get_minimum_time_slots(self):
        color_map = self.graph_coloring()
        return max(color_map.values())
n = int(input("Enter the number of subjects: "))
sub= []
stu={}
for i in range(n):
    subject = input(f"Enter subject {i + 1}: ")
    sub.append(subject)
    num = int(input(f"Enter the number of students for {subject}: "))
    st_list = [input(f"Enter student {j + 1} for {subject}: ") for j in range(num)]
    stu[subject] = st_list
g=Graph(sub)
for _ in range(int(input("Enter the number of edges: "))):
    e = input("Enter edge (subject1 subject2): ").split()
    g.add_edge(e[0], e[1])
print(f"\nMinimum time slots needed: {g.get_minimum_time_slots()}")
