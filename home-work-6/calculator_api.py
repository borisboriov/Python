from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API")

#  переменная для хранения выражения
current_expression = ""


class SimpleOperation(BaseModel):
    a: float
    b: float


class ExpressionCreate(BaseModel):
    a: float
    op: str
    b: float


class ComplexExpression(BaseModel):
    expression: str


# 1. Простые операции
@app.post("/add")
def add(op: SimpleOperation):
    return {"result": op.a + op.b}


@app.post("/subtract")
def subtract(op: SimpleOperation):
    return {"result": op.a - op.b}


@app.post("/multiply")
def multiply(op: SimpleOperation):
    return {"result": op.a * op.b}


@app.post("/divide")
def divide(op: SimpleOperation):
    if op.b == 0:
        raise HTTPException(status_code=400, detail="Division by zero")
    return {"result": op.a / op.b}


# 2. Создание выражения
@app.post("/expression/create")
def create_expression(expr: ExpressionCreate):
    global current_expression
    if expr.op not in ['+', '-', '*', '/']:
        raise HTTPException(status_code=400, detail="Invalid operator")
    current_expression = f"{expr.a} {expr.op} {expr.b}"
    return {"expression": current_expression}


# 3. Сложное выражение
@app.post("/expression/complex")
def create_complex_expression(expr: ComplexExpression):
    global current_expression
    current_expression = expr.expression
    return {"expression": current_expression}


# 4. Просмотр выражения
@app.get("/expression/current")
def get_current_expression():
    if not current_expression:
        return {"expression": None}
    return {"expression": current_expression}


# 5. Выполнение выражения
@app.post("/expression/evaluate")
def evaluate_expression():
    global current_expression
    if not current_expression:
        raise HTTPException(status_code=400, detail="No expression to evaluate")
    try:
        result = eval(current_expression)
        return {"expression": current_expression, "result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Division by zero")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid expression: {str(e)}")


# 6. Очистка
@app.delete("/expression/clear")
def clear_expression():
    global current_expression
    current_expression = ""
    return {"message": "Cleared"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
