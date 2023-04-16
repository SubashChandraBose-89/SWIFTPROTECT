import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class SwiftFieldInterview:
    agency_record_xpath = "//span[contains(text(), ' Agency Records')]"
    field_interview_xpath = "//a[contains(text(), 'Field Interviews')]"
    field_interview_title_xpath = "//h4[@class='widget-title']"
    new_FI_button_xpath = "//button[@class='btn  btn-xs btn-primary pull-right ']"
    fi_interviewDate_id = "FI_InterviewDate"
    fi_businessname_id = "FI_BusinessName"
    fi_unitnum_id = "FI_UnitNum"
    close_Alert1 = "(//span[text() = '×'])[10]"
    fi_address1_xpath = "//input[@data-control-id='FI_4929']"
    fi_state_id = "FI_State"
    fi_streetName_id = "FI_StreetName"
    fi_city_id = "FI_City"
    fi_zip_id = "FI_Zip"
    fi_txtEditr_id = "txtEditor"
    fi_detailSave_xpath = "(//*[text() = 'S'])[2]"
    fi_savedSuccessmsg_xpath = "//strong[@class='ng-binding'][@ng-bind-html='SuccessMessage']"
    switch_subjectDetails_xpath = "//a[contains(text(), 'Subject Details')]"
    fisub_new_xpath = "//button[@class='btn  btn-xs btn-primary pull-right '][@ng-click='New()']"
    addwithout_MNI_xpath = "//button[@class ='btn  btn-xs btn-primary pull-left withoutMNIHideShow']"
    fisub_subCode_id = "FISubject_SubjectCode"
    fisub_firstName_id = "FISubject_FirstName"
    fisub_ssnnum_id = "FISubject_SSNNum"
    fisub_lastName_id = "FISubject_LastName"
    fisub_middleName_id = "FISubject_MiddleName"
    fisub_alertNotes_id = "FISubject_AlertNotes"
    fisub_comment_xpath = "//textarea[@id='comments']"
    fisub_OtherDetails_xpath = "//a[contains(text(), 'Other Details')]"
    fisub_resStatus_id = 'FISubject_ResidentStatus'
    fisub_dob_id = "FISubject_DateOfBirth"
    fisub_sex_id = "FISubject_Sex"
    fisub_driLicense_id = "FISubject_DriverLicenseNum"
    fisub_ethnicity_id = "FISubject_Ethnicity"
    fisub_weg_min_xpath = "//input[@ng-model='entity.Weight']"
    fisub_weg_max_xpath = "//input[@ng-model='entity.WeightMax']"
    fisub_haircolor_id = 'FISubject_HairColor'
    fisub_hairLen_id = 'FISubject_Hairlength'
    fisub_complexion_id = 'FISubject_Complexion'
    fisub_attire_id = 'FISubject_Attire'
    fisub_scartc_id = 'FISubject_scaretc1_chosen'
    fisub_bodytype_xpath = "//li[contains(text(), 'DISCABDOM')]"
    fisub_othrResStatus_id = 'FISubject_OtherResidentStatus'
    fisub_ageMin_xpath = "//input[@ng-model='entity.Age']"
    fisub_ageMax_xpath = "//input[@ng-model='entity.AgeMax']"
    fisub_driLicState_id = 'FISubject_DriverLicenseState'
    fisub_race_id = 'FISubject_Race'
    fisub_heightFtMin_xpath = "//input[@ng-model='entity.HeightFt']"
    fisub_heightInMin_xpath = "//input[@ng-model='entity.HeightIn']"
    fisub_heightFtMax_xpath = "//input[@ng-model='entity.HeightFtMax']"
    fisub_heightInMax_xpath = "//input[@ng-model='entity.HeightInMax']"
    fisub_eyeColor_id = 'FISubject_EyeColor'
    fisub_hairStyle_id = 'FISubject_HairStyle'
    fisub_facialHair_id = 'FISubject_FacialHair'
    fisub_build_id = 'FISubject_Build'
    fisub_teeth_id = 'FISubject_Teeth'
    fisub_Address_xpath = "//a[contains(text(), 'Address')]"
    fisub_streetName_id = 'FISubject_StreetName'
    fisub_city_id = 'FISubject_City'
    fisub_alert1_xpath = "(//span[text() = '×'])[3]"
    fisub_zip_id = 'FISubject_Zip'
    fisub_cellnum_id = 'FISubject_CellPhoneNum'
    fisub_email_id = 'FISubject_Email'
    fisub_unitnum_id = 'FISubject_UnitNum'
    fisub_state_id = 'FISubject_State'
    fisub_homeNum_id = 'FISubject_HomePhoneNum'
    fisub_workNum_id = 'FISubject_WorkPhoneNum'
    fisub_VehicleDetails_xpath = "//a[contains(text(), 'Vehicle Details')]"
    fisub_plateNum_id = 'FISubject_PlateNum'
    fisub_occupant_id = 'FISubject_Occupant'
    fisub_alert2_xpath = "(//span[text() = '×'])[1]"
    fisub_makeID_id = 'FISubject_MakeID'
    fisub_selectmake_xpath = "//li[contains(text(), 'AASE - A AND A STEEL ENTERPRISES')]"
    fisub_style_id = 'FISubject_Style_chosen'
    fisub_styleSelect_xpath = "//li[contains(text(), '4 Door Sedan; Truck/pick-up 4 Door')]"
    fisub_buttomColor_id = 'FISubject_BottomColor_chosen'
    fisub_buttomColorSele_xpath = "//li[contains(text(), 'Brown')]"
    fisub_vin_id = 'FISubject_VINoan'
    fisub_vehicleYear_id = 'FISubject_VehicleYear'
    fisub_topColor_id = 'FISubject_TopColor_chosen'
    fisub_topcolorSele_xpath = "//li[contains(text(), 'Copper')]"
    fisub_plateState_id = 'FISubject_PlateState'
    fisub_saveButton_xpath = "//button[@id='btnSaveButton']"
    fisub_successMsg_xpath = "//strong[@class='ng-binding'][@ng-bind-html='SuccessMessage']"
    fisub_expText = "Field Interview Subject Details saved successfully!"
    failed_message = "Failed To Save"

    def __init__(self, driver, WebDriverWait):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def clickAgencyRecords(self):
        self.driver.find_element(By.XPATH, self.agency_record_xpath).click()

    def clickFieldInterviews(self):
        self.driver.find_element(By.XPATH, self.field_interview_xpath).click()

    def getTitle1(self):
        self.title = self.driver.find_element(By.XPATH, self.field_interview_title_xpath)
        self.title_text = self.title.text

    def clickNewFIbutton(self):
        self.driver.find_element(By.XPATH, self.new_FI_button_xpath).click()

    def setFiInterviewdata(self, fidate):
        self.driver.find_element(By.ID, self.fi_interviewDate_id).send_keys(fidate)

    def setFiBusinessname(self, businessname):
        self.driver.find_element(By.ID, self.fi_businessname_id).send_keys(businessname)

    def setFiUnitnum(self):
        self.driver.find_element(By.ID, self.fi_unitnum_id).click()

    def closeAlert1(self):
        self.driver.find_element(By.XPATH, self.close_Alert1).click()

    def setFiAddress(self, fiaddres):
        self.driver.find_element(By.XPATH, self.fi_address1_xpath).send_keys(fiaddres)

    def setFiState(self, stvalue):
        self.dropdown = Select(self.driver.find_element(By.ID, self.fi_state_id))
        self.dropdown.select_by_value(stvalue)

    def setFiStreetName(self, street):
        self.driver.find_element(By.ID, self.fi_streetName_id).send_keys(street)

    def setFiCity(self, city):
        self.driver.find_element(By.ID, self.fi_city_id).send_keys(city)

    def setFiZip(self, zip):
        self.driver.find_element(By.ID, self.fi_zip_id).send_keys(zip)

    def setFiTxtEditor(self, text):
        self.driver.find_element(By.ID, self.fi_txtEditr_id).send_keys(text)

    def clickFiSave(self):
        self.driver.find_element(By.XPATH, self.fi_detailSave_xpath).click()

    def getSuccessMsg(self):
        self.saved = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fi_savedSuccessmsg_xpath)))
        self.saved_text = self.saved.text
        print(self.saved_text)

    def disableGoogleprompt(self):
        self.driver.execute_script("Window.prototype.alert = null;")
        time.sleep(3)

    def switchToSubjectDetails(self):
        self.subject_details = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.switch_subjectDetails_xpath)))
        self.driver.execute_script("arguments[0].click();", self.subject_details)

    def clickNewDetails(self):
        self.new_details = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_new_xpath)))
        self.new_details.click()

    def addWithout_MNI(self):
        self.driver.find_element(By.XPATH, self.addwithout_MNI_xpath).click()

    def setFiSubjectCode(self):
        self.dropdown1 = Select(self.driver.find_element(By.ID, self.fisub_subCode_id))
        self.dropdown1.select_by_value("S-1")

    def setFiFirstname(self, frtname):
        self.driver.find_element(By.ID, self.fisub_firstName_id).send_keys(frtname)

    def setFiSSNnumber(self, ssn):
        self.driver.find_element(By.ID, self.fisub_ssnnum_id).send_keys(ssn)

    def setFiLastname(self, lstname):
        self.driver.find_element(By.ID, self.fisub_lastName_id).send_keys(lstname)

    def setFiMiddlename(self, mdlname):
        self.driver.find_element(By.ID, self.fisub_middleName_id).send_keys(mdlname)

    def setFiAlertnotes(self, notes):
        self.driver.find_element(By.ID, self.fisub_alertNotes_id).send_keys(notes)

    def setFiComment(self, comment):
        self.driver.find_element(By.XPATH, self.fisub_comment_xpath).send_keys(comment)
        print("Detail Form Completed")

    def switchToOtherdetails(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.fisub_OtherDetails_xpath))).click()

    def setFiResStatus(self, value):
        self.dropdown2 = Select(self.driver.find_element(By.ID, self.fisub_resStatus_id))
        self.dropdown2.select_by_value(value)

    def setFiDOB(self, dob):
        self.driver.find_element(By.ID, self.fisub_dob_id).send_keys(dob)

    def setFiSex(self, value):
        self.dropdown3 = Select(self.driver.find_element(By.ID, self.fisub_sex_id))
        self.dropdown3.select_by_value(value)

    def setFiDrivngLicn(self, licen):
        self.driver.find_element(By.ID, self.fisub_driLicense_id).send_keys(licen)

    def setFiEthnicty(self, value):
        self.dropdown4 = Select(self.driver.find_element(By.ID, self.fisub_ethnicity_id))
        self.dropdown4.select_by_value(value)

    def setFiWeightMin(self, weight):
        self.driver.find_element(By.XPATH, self.fisub_weg_min_xpath).send_keys(weight)

    def setFiWeightMax(self, weight):
        self.driver.find_element(By.XPATH, self.fisub_weg_max_xpath).send_keys(weight)

    def setFiHaircolor(self, value):
        self.dropdown5 = Select(self.driver.find_element(By.ID, self.fisub_haircolor_id))
        self.dropdown5.select_by_value(value)

    def setFiHairLen(self, value):
        self.dropdown6 = Select(self.driver.find_element(By.ID, self.fisub_hairLen_id))
        self.dropdown6.select_by_value(value)

    def setFiComplexn(self, value):
        self.dropdown7 = Select(self.driver.find_element(By.ID, self.fisub_complexion_id))
        self.dropdown7.select_by_value(value)

    def setFiAttire(self, value):
        self.dropdown8 = Select(self.driver.find_element(By.ID, self.fisub_attire_id))
        self.dropdown8.select_by_value(value)

    def setFiScartchn(self):
        self.driver.find_element(By.ID, self.fisub_scartc_id).click()

    def setFiType(self):
        self.driver.find_element(By.XPATH, self.fisub_bodytype_xpath).click()

    def setFiOthrResStatus(self, resdnt):
        self.driver.find_element(By.ID, self.fisub_othrResStatus_id).send_keys(resdnt)

    def setFiAgeMin(self, age):
        self.driver.find_element(By.XPATH, self.fisub_ageMin_xpath).send_keys(age)

    def setfiAgemax(self, age):
        self.driver.find_element(By.XPATH, self.fisub_ageMax_xpath).send_keys(age)

    def setFiDriLicState(self, value):
        self.dropdown9 = Select(self.driver.find_element(By.ID, self.fisub_driLicState_id))
        self.dropdown9.select_by_value(value)

    def setFiRace(self, value):
        self.dropdown10 = Select(self.driver.find_element(By.ID, self.fisub_race_id))
        self.dropdown10.select_by_value(value)

    def setFiHeightFtMin(self, ft):
        self.driver.find_element(By.XPATH, self.fisub_heightFtMin_xpath).send_keys(ft)

    def setFiHeighInMin(self, inch):
        self.driver.find_element(By.XPATH, self.fisub_heightInMin_xpath).send_keys(inch)

    def setFiHeightFtMax(self, ft):
        self.driver.find_element(By.XPATH, self.fisub_heightFtMax_xpath).send_keys(ft)

    def setFiHeighInMax(self, inch):
        self.driver.find_element(By.XPATH, self.fisub_heightInMax_xpath).send_keys(inch)

    def setFiEyecolor(self, value):
        self.dropdown11 = Select(self.driver.find_element(By.ID, self.fisub_eyeColor_id))
        self.dropdown11.select_by_value(value)

    def setFiHairStyle(self, value):
        self.dropdown12 = Select(self.driver.find_element(By.ID, self.fisub_hairStyle_id))
        self.dropdown12.select_by_value(value)

    def setFiFacialHair(self, value):
        self.dropdown13 = Select(self.driver.find_element(By.ID, self.fisub_facialHair_id))
        self.dropdown13.select_by_value(value)

    def setFiBuild(self, value):
        self.dropdown14 = Select(self.driver.find_element(By.ID, self.fisub_build_id))
        self.dropdown14.select_by_value(value)

    def setFiTeeth(self, value):
        self.dropdown15 = Select(self.driver.find_element(By.ID, self.fisub_teeth_id))
        self.dropdown15.select_by_value(value)

    def switchToAddress(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.fisub_Address_xpath))).click()

    def setFiStreetname(self, name):
        self.driver.find_element(By.ID, self.fisub_streetName_id).send_keys(name)

    def setFiSubCity(self):
        self.driver.find_element(By.ID, self.fisub_city_id).click()

    def clickAlert3(self):
        self.driver.find_element(By.XPATH, self.fisub_alert1_xpath).click()

    def setFiSubCity1(self, city):
        self.driver.find_element(By.ID, self.fisub_city_id).send_keys(city)

    def setFiSubZip(self, szip):
        self.driver.find_element(By.ID, self.fisub_zip_id).send_keys(szip)

    def setFiCellnum(self, number):
        self.driver.find_element(By.ID, self.fisub_cellnum_id).send_keys(number)

    def setFiEmail(self, email):
        self.driver.find_element(By.ID, self.fisub_email_id).send_keys(email)

    def setFiUnitNumber(self, number):
        self.driver.find_element(By.ID, self.fisub_unitnum_id).send_keys(number)

    def setFiSubState(self, value):
        self.dropdown16 = Select(self.driver.find_element(By.ID, self.fisub_state_id))
        self.dropdown16.select_by_value(value)

    def setFiHomeNumber(self, number):
        self.driver.find_element(By.ID, self.fisub_homeNum_id).send_keys(number)

    def setFiWorkNumber(self, number):
        self.driver.find_element(By.ID, self.fisub_workNum_id).send_keys(number)
        print("Address Form Completed")

    def switchToVehicleDetails(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.fisub_VehicleDetails_xpath))).click()

    def setFiPlateNum(self, number):
        self.driver.find_element(By.ID, self.fisub_plateNum_id).send_keys(number)

    def setFiOccupant(self):
        self.driver.find_element(By.ID, self.fisub_occupant_id).click()

    def clickAlert4(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_alert2_xpath))).click()

    def setFiOccupant1(self, name):
        self.driver.find_element(By.ID, self.fisub_occupant_id).send_keys(name)

    def setFiMakeID(self, name):
        self.driver.find_element(By.ID, self.fisub_makeID_id).send_keys(name)

    def setFiMakeID1(self):
        self.driver.find_element(By.ID, self.fisub_makeID_id).click()

    def setFiMakeIDSelect(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_selectmake_xpath))).click()

    def setFiStyleChosen(self):
        self.driver.find_element(By.ID, self.fisub_style_id).click()

    def setFiStyleSelect(self):
        self.style = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_styleSelect_xpath)))
        self.style.click()

    def setFiButtomColor(self):
        self.driver.find_element(By.ID, self.fisub_buttomColor_id).click()

    def setFiButtomSelect(self):
        self.bottom_color = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_buttomColorSele_xpath)))
        self.bottom_color.click()

    def setFiVIN(self, vin):
        self.driver.find_element(By.ID, self.fisub_vin_id).send_keys(vin)

    def setFiVehicleYear(self, year):
        self.driver.find_element(By.ID, self.fisub_vehicleYear_id).send_keys(year)

    def setFiTopcolor(self):
        self.driver.find_element(By.ID, self.fisub_topColor_id).click()

    def setFiTopcolorSelect(self):
        self.top_color = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_topcolorSele_xpath)))
        self.top_color.click()

    def setFiPlateState(self, value):
        self.dropdown17 = Select(self.driver.find_element(By.ID, self.fisub_plateState_id))
        self.dropdown17.select_by_value(value)

    def setFiFinalButSave(self):
        self.driver.find_element(By.XPATH, self.fisub_saveButton_xpath).click()

    def setFiSuccessMsg(self):
        self.success_msg = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.fisub_successMsg_xpath)))
        self.success_msg_text = self.success_msg.text
        self.actual_text = self.success_msg_text
        self.expected_text = self.fisub_expText
        if self.actual_text == self.expected_text:
            print(self.success_msg_text)
        else:
            print(self.failed_message)
