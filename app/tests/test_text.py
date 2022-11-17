from text import TextElements


class TestText:
    def test_if_return_text_return_right_value(self):
        test_text_elements = TextElements(text='test_text', status='test_status', rot_type='test_rot_type')
        assert test_text_elements.return_text() == 'test_text'
