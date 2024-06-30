/*
 Navicat Premium Data Transfer

 Source Server         : dbfinal
 Source Server Type    : MySQL
 Source Server Version : 80300 (8.3.0)
 Source Host           : localhost:3306
 Source Schema         : db

 Target Server Type    : MySQL
 Target Server Version : 80300 (8.3.0)
 File Encoding         : 65001

 Date: 01/06/2024 17:53:34
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for Diagnosis
-- ----------------------------
DROP TABLE IF EXISTS `Diagnosis`;
CREATE TABLE `Diagnosis` (
  `DoctorID` varchar(30) NOT NULL,
  `PatientID` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `PrescriptionID` varchar(30) NOT NULL,
  `DiagnosisDate` date DEFAULT NULL,
  PRIMARY KEY (`DoctorID`,`PatientID`,`PrescriptionID`),
  KEY `PatientID` (`PatientID`),
  KEY `PrescriptionID` (`PrescriptionID`),
  CONSTRAINT `fk_diagnosis_doctor` FOREIGN KEY (`DoctorID`) REFERENCES `Doctor` (`DoctorID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_diagnosis_patient` FOREIGN KEY (`PatientID`) REFERENCES `Patient` (`PatientID`),
  CONSTRAINT `fk_diagnosis_prescription` FOREIGN KEY (`PrescriptionID`) REFERENCES `Prescription` (`PrescriptionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Diagnosis
-- ----------------------------
BEGIN;
INSERT INTO `Diagnosis` (`DoctorID`, `PatientID`, `PrescriptionID`, `DiagnosisDate`) VALUES ('2', '1923898912892', '214421', '2024-05-18');
INSERT INTO `Diagnosis` (`DoctorID`, `PatientID`, `PrescriptionID`, `DiagnosisDate`) VALUES ('2', '2189038901829', '31299', '2024-05-18');
INSERT INTO `Diagnosis` (`DoctorID`, `PatientID`, `PrescriptionID`, `DiagnosisDate`) VALUES ('555', '2189038901829', '61013', '2024-05-28');
INSERT INTO `Diagnosis` (`DoctorID`, `PatientID`, `PrescriptionID`, `DiagnosisDate`) VALUES ('555', '666', '123', '2024-05-26');
INSERT INTO `Diagnosis` (`DoctorID`, `PatientID`, `PrescriptionID`, `DiagnosisDate`) VALUES ('555', '666', '520', '2024-05-27');
INSERT INTO `Diagnosis` (`DoctorID`, `PatientID`, `PrescriptionID`, `DiagnosisDate`) VALUES ('555', '666', '777', '2024-05-09');
COMMIT;

-- ----------------------------
-- Table structure for Doctor
-- ----------------------------
DROP TABLE IF EXISTS `Doctor`;
CREATE TABLE `Doctor` (
  `DoctorID` varchar(30) NOT NULL,
  `Degree` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`DoctorID`),
  CONSTRAINT `fk_doctor_staff` FOREIGN KEY (`DoctorID`) REFERENCES `Staff` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Doctor
-- ----------------------------
BEGIN;
INSERT INTO `Doctor` (`DoctorID`, `Degree`) VALUES ('1125', '资深医师');
INSERT INTO `Doctor` (`DoctorID`, `Degree`) VALUES ('2', '普通医师');
INSERT INTO `Doctor` (`DoctorID`, `Degree`) VALUES ('555', '主治医师');
COMMIT;

-- ----------------------------
-- Table structure for Medicine
-- ----------------------------
DROP TABLE IF EXISTS `Medicine`;
CREATE TABLE `Medicine` (
  `MedicineID` varchar(30) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Price` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`MedicineID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Medicine
-- ----------------------------
BEGIN;
INSERT INTO `Medicine` (`MedicineID`, `Name`, `Price`) VALUES ('13', '尿不湿', 1.50);
INSERT INTO `Medicine` (`MedicineID`, `Name`, `Price`) VALUES ('14', '999感冒灵', 19.30);
INSERT INTO `Medicine` (`MedicineID`, `Name`, `Price`) VALUES ('50', '金嗓子喉片', 5.00);
INSERT INTO `Medicine` (`MedicineID`, `Name`, `Price`) VALUES ('66', '金嗓子喉片', 6.00);
INSERT INTO `Medicine` (`MedicineID`, `Name`, `Price`) VALUES ('78', '金嗓子喉片', 3.55);
COMMIT;

-- ----------------------------
-- Table structure for Nurse
-- ----------------------------
DROP TABLE IF EXISTS `Nurse`;
CREATE TABLE `Nurse` (
  `NurseID` varchar(30) NOT NULL,
  `Certification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`NurseID`),
  CONSTRAINT `fk_nurse_staff` FOREIGN KEY (`NurseID`) REFERENCES `Staff` (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Nurse
-- ----------------------------
BEGIN;
INSERT INTO `Nurse` (`NurseID`, `Certification`) VALUES ('2763', '护士长');
COMMIT;

-- ----------------------------
-- Table structure for Patient
-- ----------------------------
DROP TABLE IF EXISTS `Patient`;
CREATE TABLE `Patient` (
  `PatientID` varchar(30) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Number` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Patient
-- ----------------------------
BEGIN;
INSERT INTO `Patient` (`PatientID`, `Name`, `Gender`, `Age`, `Number`) VALUES ('1923898912892', '李博瑞', '男', 28, '1203012803');
INSERT INTO `Patient` (`PatientID`, `Name`, `Gender`, `Age`, `Number`) VALUES ('2189038901829', '王二狗', '女', 8, '1381247098');
INSERT INTO `Patient` (`PatientID`, `Name`, `Gender`, `Age`, `Number`) VALUES ('444', '含姐', '女', 20, '120');
INSERT INTO `Patient` (`PatientID`, `Name`, `Gender`, `Age`, `Number`) VALUES ('666', '王檄烨', '女', 20, '110');
INSERT INTO `Patient` (`PatientID`, `Name`, `Gender`, `Age`, `Number`) VALUES ('810329321', '李三', '男', 54, '12031823823');
COMMIT;

-- ----------------------------
-- Table structure for Prescript
-- ----------------------------
DROP TABLE IF EXISTS `Prescript`;
CREATE TABLE `Prescript` (
  `PrescriptionID` varchar(30) NOT NULL,
  `MedicineID` varchar(30) NOT NULL,
  PRIMARY KEY (`PrescriptionID`,`MedicineID`),
  KEY `MedicineID` (`MedicineID`),
  CONSTRAINT `fk_prescript_medicine` FOREIGN KEY (`MedicineID`) REFERENCES `Medicine` (`MedicineID`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `fk_prescript_prescription` FOREIGN KEY (`PrescriptionID`) REFERENCES `Prescription` (`PrescriptionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Prescript
-- ----------------------------
BEGIN;
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('777', '13');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('777', '14');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('123', '50');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('520', '50');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('777', '50');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('123', '66');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('520', '66');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('123', '78');
INSERT INTO `Prescript` (`PrescriptionID`, `MedicineID`) VALUES ('520', '78');
COMMIT;

-- ----------------------------
-- Table structure for Prescription
-- ----------------------------
DROP TABLE IF EXISTS `Prescription`;
CREATE TABLE `Prescription` (
  `PrescriptionID` varchar(30) NOT NULL,
  `Symptom` text,
  `advice` text,
  PRIMARY KEY (`PrescriptionID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Prescription
-- ----------------------------
BEGIN;
INSERT INTO `Prescription` (`PrescriptionID`, `Symptom`, `advice`) VALUES ('123', '太聪明', '多玩消消乐');
INSERT INTO `Prescription` (`PrescriptionID`, `Symptom`, `advice`) VALUES ('214421', '月经不调', '挂内分泌科');
INSERT INTO `Prescription` (`PrescriptionID`, `Symptom`, `advice`) VALUES ('31299', '窜稀', '绝食');
INSERT INTO `Prescription` (`PrescriptionID`, `Symptom`, `advice`) VALUES ('520', '相思病', '喝水');
INSERT INTO `Prescription` (`PrescriptionID`, `Symptom`, `advice`) VALUES ('61013', '尿血', '枸杞泡水');
INSERT INTO `Prescription` (`PrescriptionID`, `Symptom`, `advice`) VALUES ('777', '背部红点', '抹药');
COMMIT;

-- ----------------------------
-- Table structure for Staff
-- ----------------------------
DROP TABLE IF EXISTS `Staff`;
CREATE TABLE `Staff` (
  `StaffID` varchar(30) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Position` varchar(50) DEFAULT NULL,
  `Department` varchar(50) DEFAULT NULL,
  `userpassword` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`StaffID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of Staff
-- ----------------------------
BEGIN;
INSERT INTO `Staff` (`StaffID`, `Name`, `Gender`, `Position`, `Department`, `userpassword`) VALUES ('1', '2', '3', '4', '5', NULL);
INSERT INTO `Staff` (`StaffID`, `Name`, `Gender`, `Position`, `Department`, `userpassword`) VALUES ('1125', '王檄烨', '女', '医生', '皮肤科', '031105');
INSERT INTO `Staff` (`StaffID`, `Name`, `Gender`, `Position`, `Department`, `userpassword`) VALUES ('11253', '32321', '321321', '2332', '2313', '123456');
INSERT INTO `Staff` (`StaffID`, `Name`, `Gender`, `Position`, `Department`, `userpassword`) VALUES ('2', '沈亚楠', '女', '医生', '肛肠科', '123456');
INSERT INTO `Staff` (`StaffID`, `Name`, `Gender`, `Position`, `Department`, `userpassword`) VALUES ('2763', '含姐', '女', '护士', '脑科', '000000');
INSERT INTO `Staff` (`StaffID`, `Name`, `Gender`, `Position`, `Department`, `userpassword`) VALUES ('555', '申宗尚', '男', '医生', '泌尿科', '040620');
COMMIT;

-- ----------------------------
-- View structure for diagnosisinfo
-- ----------------------------
DROP VIEW IF EXISTS `diagnosisinfo`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `diagnosisinfo` AS select `d`.`PrescriptionID` AS `PrescriptionID`,`d`.`DiagnosisDate` AS `DiagnosisDate`,`st`.`Department` AS `Department`,`st`.`Name` AS `DocName`,`p`.`PatientID` AS `PatID`,`p`.`Name` AS `PatName`,`r`.`Symptom` AS `Symptom`,`r`.`advice` AS `advice` from (((`diagnosis` `d` join `staff` `st` on((`d`.`DoctorID` = `st`.`StaffID`))) join `patient` `p` on((`d`.`PatientID` = `p`.`PatientID`))) join `prescription` `r` on((`d`.`PrescriptionID` = `r`.`PrescriptionID`)));

-- ----------------------------
-- Procedure structure for UpdateDiagnosis
-- ----------------------------
DROP PROCEDURE IF EXISTS `UpdateDiagnosis`;
delimiter ;;
CREATE PROCEDURE `UpdateDiagnosis`(IN p_PrescriptionID VARCHAR(30),
    IN p_Symptom TEXT,
    IN p_advice TEXT,
    IN p_DoctorName VARCHAR(100),
    IN p_PatientID VARCHAR(30),
    IN p_DiagnosisDate DATE)
BEGIN
    DECLARE v_DoctorID INT;
    DECLARE v_Exists INT;
    DECLARE v_CurrentDate DATE;

    -- 获取当前日期
    SET v_CurrentDate = CURDATE();

    -- 检查 DiagnosisDate 是否在 2022 年之后和当前日期之前
    IF p_DiagnosisDate < '2022-01-01' OR p_DiagnosisDate > v_CurrentDate THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'DiagnosisDate必须在2022年到当前日期之间';
    END IF;

    -- 获取医生的StaffID
    SELECT StaffID INTO v_DoctorID
    FROM Staff
    WHERE Name = p_DoctorName
    AND Position = '医生';

    IF v_DoctorID IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = '医生未找到';
    END IF;

    -- 使用表连接检查 Prescription 是否存在
    SELECT COUNT(*) INTO v_Exists
    FROM Prescription p
    JOIN Diagnosis d ON p.PrescriptionID = d.PrescriptionID
    WHERE p.PrescriptionID = p_PrescriptionID;

    IF v_Exists = 0 THEN
        -- 插入 Prescription 表和 Diagnosis 表
        INSERT INTO Prescription (PrescriptionID, Symptom, advice)
        VALUES (p_PrescriptionID, p_Symptom, p_advice);

        INSERT INTO Diagnosis (DoctorID, PatientID, PrescriptionID, DiagnosisDate)
        VALUES (v_DoctorID, p_PatientID, p_PrescriptionID, p_DiagnosisDate);
    ELSE
        -- 更新 Prescription 表和 Diagnosis 表
        UPDATE Prescription p
        JOIN Diagnosis d ON p.PrescriptionID = d.PrescriptionID
        SET p.Symptom = p_Symptom, p.advice = p_advice, d.DiagnosisDate = p_DiagnosisDate
        WHERE p.PrescriptionID = p_PrescriptionID;
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Diagnosis
-- ----------------------------
DROP TRIGGER IF EXISTS `check_diagnosis_insert`;
delimiter ;;
CREATE TRIGGER `check_diagnosis_insert` BEFORE INSERT ON `Diagnosis` FOR EACH ROW BEGIN
    IF NEW.DiagnosisDate < '2022-01-01' OR NEW.DiagnosisDate > CURRENT_DATE THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'DiagnosisDate必须在2022年到当前日期之间';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Diagnosis
-- ----------------------------
DROP TRIGGER IF EXISTS `check_diagnosis_update`;
delimiter ;;
CREATE TRIGGER `check_diagnosis_update` BEFORE UPDATE ON `Diagnosis` FOR EACH ROW BEGIN
    IF NEW.DiagnosisDate < '2022-01-01' OR NEW.DiagnosisDate > CURRENT_DATE THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'DiagnosisDate必须在2022年到当前日期之间';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Patient
-- ----------------------------
DROP TRIGGER IF EXISTS `check_gender_kind`;
delimiter ;;
CREATE TRIGGER `check_gender_kind` BEFORE INSERT ON `Patient` FOR EACH ROW BEGIN
    IF NEW.Gender <> '男' AND NEW.Gender <> '女' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '性别填写错误！';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Patient
-- ----------------------------
DROP TRIGGER IF EXISTS `check_age_num`;
delimiter ;;
CREATE TRIGGER `check_age_num` BEFORE INSERT ON `Patient` FOR EACH ROW BEGIN
    IF NEW.Age < 0 OR NEW.Age > 200 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '年龄填写错误！';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Patient
-- ----------------------------
DROP TRIGGER IF EXISTS `check_gender_kind_update`;
delimiter ;;
CREATE TRIGGER `check_gender_kind_update` BEFORE UPDATE ON `Patient` FOR EACH ROW BEGIN
    IF NEW.Gender <> '男' AND NEW.Gender <> '女' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '性别填写错误！';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Patient
-- ----------------------------
DROP TRIGGER IF EXISTS `check_age_num_update`;
delimiter ;;
CREATE TRIGGER `check_age_num_update` BEFORE UPDATE ON `Patient` FOR EACH ROW BEGIN
    IF NEW.Age < 0 OR NEW.Age > 200 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = '年龄填写错误！';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Prescription
-- ----------------------------
DROP TRIGGER IF EXISTS `check_prescription_insert`;
delimiter ;;
CREATE TRIGGER `check_prescription_insert` BEFORE INSERT ON `Prescription` FOR EACH ROW BEGIN
    IF LENGTH(NEW.PrescriptionID) < 1 OR LENGTH(NEW.PrescriptionID) > 15 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'PrescriptionID长度必须大于等于1且小于等于15';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Prescription
-- ----------------------------
DROP TRIGGER IF EXISTS `check_prescription_update`;
delimiter ;;
CREATE TRIGGER `check_prescription_update` BEFORE UPDATE ON `Prescription` FOR EACH ROW BEGIN
    IF LENGTH(NEW.PrescriptionID) < 1 OR LENGTH(NEW.PrescriptionID) > 15 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'PrescriptionID长度必须大于等于1且小于等于15';
    END IF;
END
;;
delimiter ;

-- ----------------------------
-- Triggers structure for table Staff
-- ----------------------------
DROP TRIGGER IF EXISTS `after_staff_insert`;
delimiter ;;
CREATE TRIGGER `after_staff_insert` AFTER INSERT ON `Staff` FOR EACH ROW BEGIN
    IF NEW.Position = '医生' THEN
        INSERT INTO Docter (DocterID, Degree)
        VALUES (NEW.StaffID, '');
    ELSEIF NEW.Position = '护士' THEN
        INSERT INTO Nurse (NurseID, Certification)
        VALUES (NEW.StaffID, '');
    END IF;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
