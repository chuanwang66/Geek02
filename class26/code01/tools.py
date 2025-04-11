from langchain_core.tools import tool

@tool
def modelsTool(model_name: str):
    """该工具可用于生成实体类代码"""

    model_name = model_name.lower()

    if "user" or "用户" in model_name:
        return """
type UserModel struct
{
    UserID int64 `json:"user_id"`
    UserName string `json:"user_name"`
    UserEmail string `json:"user_email"`
}        
"""
    return ""

