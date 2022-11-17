import pytest
from rot import Rot13, Rot47, RotFactory, RotManager


class TestRot47AndRot13Class:

    @pytest.mark.parametrize('text, coded', [('aaa', 'nnn'), ('bbb', 'ooo'), ('zzz', 'mmm')])
    def test_if_class_13_encode_return_right_value(self, text, coded):
        rot13 = Rot13()
        assert rot13.encode(text_to_encode=text) == [coded, 'encoded']

    @pytest.mark.parametrize('text, coded', [('nnn', 'aaa'), ('ooo', 'bbb'), ('mmm', 'zzz')])
    def test_if_class_13_decode_return_right_value(self, text, coded):
        rot13 = Rot13()
        assert rot13.decode(text_to_decode=text) == [coded, 'decoded']

    def test_if_rot13_return_right_rot_type(self):
        rot13 = Rot13()
        assert rot13.rot_type() == 'rot13'

    @pytest.mark.parametrize('text, coded', [('aaa', 'vvv'), ('bbb', 'www'), ('eee', 'zzz')])
    def test_if_class_47_encode_return_right_value(self, text, coded):
        rot47 = Rot47()
        assert rot47.encode(text_to_encode=text) == [coded, 'encoded']

    @pytest.mark.parametrize('text, coded', [('vvv', 'aaa'), ('www', 'bbb'), ('zzz', 'eee')])
    def test_if_class_47_decode_return_right_value(self, text, coded):
        rot47 = Rot47()
        assert rot47.decode(text_to_decode=text) == [coded, 'decoded']

    def test_if_rot47_return_right_rot_type(self):
        rot47 = Rot47()
        assert rot47.rot_type() == 'rot47'


class TestRotFactoryClass:
    def test_if_rot_factory_return_right_rot13_class(self):
        assert type(RotFactory.get_rot(shift='13')) == type(Rot13())

    def test_if_rot_factory_return_right_rot47_class(self):
        assert type(RotFactory.get_rot(shift='47')) == type(Rot47())


class TestRotManager:
    def test_if_rot_menu_print_right_text(self, capsys):
        RotManager.rot_menu()
        captured = capsys.readouterr()
        assert captured.out == "ROT MENU: \n" \
                               "For encrypt own text in Rot13 enter - 1 \n" \
                               "For decrypt own text in Rot13 enter - 2 \n" \
                               "For encrypt own text in Rot47 enter - 3 \n" \
                               "For decrypt own text in Rot47 enter - 4 \n" \
                               "For use element from buffer enter - 5\n" \
                               "\n"

