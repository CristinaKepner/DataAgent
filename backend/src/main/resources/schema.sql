CREATE TABLE dataset (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE data_item (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    dataset_id BIGINT NOT NULL,
    content TEXT NOT NULL,
    status VARCHAR(50) DEFAULT 'PENDING',
    FOREIGN KEY (dataset_id) REFERENCES dataset(id)
);

CREATE TABLE annotation (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    item_id BIGINT NOT NULL,
    annotator_id BIGINT NOT NULL,
    result JSON NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES data_item(id)
);

CREATE TABLE error_patterns (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    case_type VARCHAR(100) NOT NULL,
    pattern JSON NOT NULL,  # 存储错误模式知识图谱
    solution TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE annotation ADD COLUMN confidence_score FLOAT DEFAULT 1.0;