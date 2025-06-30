-- UTF-8 문자셋 설정 (한글 인코딩 깨짐 방지)
SET NAMES utf8mb4;

-- 테이블 생성
CREATE TABLE GLOSSARY (
    id INT AUTO_INCREMENT PRIMARY KEY,
    short_eng_nm VARCHAR(50) NOT NULL,
    eng_nm VARCHAR(50) NOT NULL,
    kor_nm VARCHAR(50) NOT NULL,
    description TEXT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- 데이터 삽입
INSERT INTO GLOSSARY (short_eng_nm, eng_nm, kor_nm, description) VALUES
('acc', 'account', '계좌', '금융 거래를 위해 개설하는 예금, 투자, 대출 등을 관리하는 금융 계정'),
('mgn', 'margin', '증거금', '주식이나 파생상품 거래 시 거래 이행을 보장하기 위해 거래 전에 미리 납부하는 보증금'),
('ord', 'order', '주문', '투자자가 증권 시장에서 매수 또는 매도하고자 하는 의사를 표시하는 것'),
('exec', 'execution', '체결', '계약, 합의, 또는 거래 등이 성립되어 효력을 발생하는 것을 의미'),
('fut', 'futures', '선물', '파생상품의 일종으로, 미래 일정 시점에 특정 상품이나 금융 자산을 미리 정해진 가격으로 거래하는 계약'),
('opt', 'option', '옵션', '특정 자산(기초자산)을 미래 특정 시점에 미리 정해진 가격으로 사고팔 수 있는 권리를 거래하는 계약');
