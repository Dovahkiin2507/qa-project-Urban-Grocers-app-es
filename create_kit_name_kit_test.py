import data
import sender_stand_request

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body
def possitive_assert(kit_name):
    kit_name = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_name)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == kit_name["name"]
def negative_assert_code_400(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400
def negative_assert_no_name(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

def test_create_user_kit_1_letter_in_name_get_success_response():
    possitive_assert("a")
def test_create_user_kit_511_letter_in_name_get_success_response():
    possitive_assert("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                     "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "abcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                     "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                     "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcda"
                     "bcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                     "bcdabcdabcdabC")
def test_create_user_kit_empty_letter_in_name_get_error_response():
    negative_assert_code_400("")
def test_create_user_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400("Abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabc"
                             "dabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab"
                             "cdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcd"
                             "abcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdab")
def test_create_user_kit_has_special_symbol_in_name_get_success_response():
    possitive_assert("№%@,")
def test_create_user_kit_has_space_in_name_get_success_response():
    possitive_assert(" A Aaa ")
def test_create_user_kit_has_number_in_name_get_success_response():
    possitive_assert("123")
def test_create_user_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)
def test_create_user_kit_number_type_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400