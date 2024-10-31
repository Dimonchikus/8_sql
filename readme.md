### Швидкість читання залежно від індексів
SELECT * FROM users WHERE date_of_birth between '1990-03-11' and '1999-05-11';

**Without index:**  
Time: 2.16 sec

**With BTree index (`CREATE INDEX idx_btree_dob ON users(date_of_birth) USING BTREE;`):**  
Time: 0.5

**With Hash index (`CREATE INDEX idx_dob_hash ON users(date_of_birth) USING HASH;`):** _- for my surprise it worked (as we know hash doesn't support anymore)_  
Time: 0.65 sec

### Швидкість запису в залежності від innodb_flush_log_at_trx_commit (використовував той же insert_users.py)

Запис 500000 записів

**SET GLOBAL innodb_flush_log_at_trx_commit = 2;**  
Time: 69 sec

**SET GLOBAL innodb_flush_log_at_trx_commit = 1;**  
Time: 88 sec

**SET GLOBAL innodb_flush_log_at_trx_commit = 0;**  
Time: 95 sec