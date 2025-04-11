from langgraph.graph import StateGraph, START,END

def supermarket(state):
    return {"ret": "{}买到了".format(state["ingredients"])}

if __name__ == "__main__":
    sg = StateGraph(dict)

    # 定义节点
    sg.add_node("supermarket", supermarket)

    # 定义起始边
    sg.add_edge(START, "supermarket")

    # 定义结束边
    sg.add_edge("supermarket", END)

    graph = sg.compile()
    ret = graph.invoke({"ingredients": "羊排"})

    print(ret)
    
