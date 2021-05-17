def getNodeWordSet(node, graph, numberOfWords=50, debug=False):
    """
    For the node named nodeName in the graph searches BFS for words representing this word.
    """
    resultSet = set()
    alreadySeenNodes = set()

    bfsQueue = [node]

    while len(resultSet) < 50 and bfsQueue:
        currentNode = bfsQueue.pop()
        alreadySeenNodes.add(currentNode)

        currentNodeName = currentNode[9:]
        if debug:
            print("Currently visiting:", currentNodeName)
        # Adds current node words
        words = currentNodeName.split()
        for word in words:
            if len(resultSet) < numberOfWords:
                resultSet.add(word.lower())

        neighbors = [i for i in graph.getNeighbors(
            currentNode) if i not in alreadySeenNodes]
        for neighbourNode in neighbors:
            bfsQueue.insert(0, neighbourNode)

    return list(resultSet)
