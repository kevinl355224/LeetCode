from typing import List
from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        """
        1 <= paths.length <= 2 * 10**4
        1 <= paths[i].length <= 500
        1 <= paths[i][j].length <= 10
        1 <= sum(paths[i][j].length) <= 2 * 10**5

        Each folder name is unique.
        """
        class TrieNode:
            def __init__(self, name):
                self.name = name
                self.children = {}
                self.signature = ""

        # Build a trie node for all path
        root = TrieNode("")
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode(folder)
                node = node.children[folder]

        signature_cnt = defaultdict(int)

        # Add child-folder signature into node through dfs
        def dfs(node):
            if not node.children:
                node.signature = ""
                return ""
            child_signatures = []
            for name, child in sorted(node.children.items()):
                child_signature = dfs(child)
                child_signatures.append(f"{name}({child_signature})")

            node.signature = "".join(child_signatures)
            signature_cnt[node.signature] += 1
            return node.signature
        dfs(root)

        result = []
        current_path = []

        # Use to valid folder
        def dfs2(node):
            # If node has child folder and there is other folder has same structure.
            if node.children and signature_cnt[node.signature] >= 2:
                return
            # Get into the folder
            print(node.name)
            current_path.append(node.name)
            result.append(current_path.copy())
            for name, child in sorted(node.children.items()):
                dfs2(child)
            # Go out of the folder
            current_path.pop()

        for name, child in sorted(root.children.items()):
            dfs2(child)

        return result

if __name__ == "__main__":
    sol = Solution()
    paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
    print(sol.deleteDuplicateFolder(paths))
