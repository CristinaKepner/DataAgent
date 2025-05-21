import sqlite3
from typing import List

class CoTAnnotator:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self._init_db()
    
    def _init_db(self):
        # 创建错误案例数据库
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS error_cases (
            id INTEGER PRIMARY KEY,
            case_type TEXT,
            pattern TEXT,
            solution TEXT
        )
        """)
    
    def analyze_errors(self, new_errors: List[dict]):
        # 动态分析错误模式
        for error in new_errors:
            self.conn.execute(
                "INSERT INTO error_cases VALUES (?, ?, ?, ?)",
                (None, error["type"], str(error["pattern"]), error["solution"])
            )
        self.conn.commit()