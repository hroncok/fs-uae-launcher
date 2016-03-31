from fsui.qt import QSpinBox
from .widget_mixin import WidgetMixin


class SpinCtrl(WidgetMixin):

    def __init__(self, parent, min_value, max_value, initial_value):
        self._widget = QSpinBox(parent.get_container())
        # Widget.__init__(self, parent)
        self.init_widget(parent)
        self._widget.setRange(min_value, max_value)
        self._widget.setValue(initial_value)
        self._widget.valueChanged.connect(self.__value_changed)

    def get_value(self):
        return self._widget.value()

    def set_value(self, value):
        self._widget.setValue(value)

    def __value_changed(self, _):
        self.on_changed()

    def on_change(self):
        pass
