# Things that need to be added according to the rubric
Going to rewrite the examples from class for easier access

#### Stored Fuction
```
drop function IF EXISTS InstructorLevel;

DELIMITER $$

CREATE FUNCTION InstructorLevel(p_salary double) RETURNS VARCHAR(20)
BEGIN
    DECLARE lvl VARCHAR(20);

    IF p_salary > 1000000 THEN
        SET lvl = 'SIX FIGURES';
    ELSE
        SET lvl = 'NOT SIX FIGURES';
    END IF;

  RRTURN (lvl);
END $$
```

#### Procedure
```
drop procedure IF EXISTS CountProducts;

DELIMITER $$

CREATE PROCEDURE CountProducts(in threshold integer, out prod_count integer)
  BEGIN
  SELECT count(*) into prod_count FROM FK_product where price > threshold;
  END $$
```

#### Trigger
```
CREATE TABLE people (age INT, name VARCHAR(150));

CREATE TRIGGER agecheck BEFORE INSERT ON people
FOR EACH ROW
    BEGIN
        IF NEW.age < 18 THEN
        SET NEW.age = 18;
        END IF;
    END;
```

```
CREATE TRIGGER update_credit AFTER UPDATE ON course
    FOR EACH NOW
    BEGIN
        IF NEW.credits <> OLD.credits THEN
            UPDATE student
            SET tot_cred = tot_cred - OLD.credits + NEW.credits
            WHERE student.ID in
            (select id fromt takes where course_id = NEW.course_id and takes.grade <> 'F' and takes.grade is not null);
        END IF;
    END;
```
