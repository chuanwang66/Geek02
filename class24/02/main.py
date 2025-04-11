from langgraph.graph import StateGraph, START,END

def supermarket(state):
    print("supermarket")
    return {"ret": "{}买到了".format(state["ingredients"])}

def recipe(state):
    print("recipe")
    #return {"ret": "搜到了菜谱"}
    return {"ret": "搜到了红烧{}的菜谱".format(state["ingredients"])}

def cooking(state):
    print("cooking")
    #return {"ret": "做了一道菜"}
    return {"ret": "做了一道红烧{}".format(state["ingredients"])}

if __name__ == "__main__":
    sg = StateGraph(dict)

    # 定义节点
    sg.add_node("supermarket", supermarket)
    sg.add_node("recipe", recipe)
    sg.add_node("cooking", cooking)

    # 定义起始边
    sg.add_edge(START, "supermarket")

    # 定义普通边
    sg.add_edge("supermarket", "recipe")
    sg.add_edge("recipe", "cooking")

    # 定义结束边
    sg.add_edge("cooking", END)

    graph = sg.compile()
    ret = graph.invoke({"ingredients": "羊排"})

    print(ret)
    
