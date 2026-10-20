def parse_student(line):
    fields = line.strip().split(",")
    if len(fields) != 2:
        raise ValueError(f"字段数量错误，应为 2 个，实际 {len(fields)} 个")
    name, score_text = fields[0].strip(), fields[1].strip()
    if not name:
        raise ValueError("姓名不能为空")
    try:
        score = int(score_text)
    except ValueError:
        raise ValueError(f"成绩无法转换为整数: {score_text!r}")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩 {score} 超出 0~100 范围")
    return {"name": name, "score": score}
