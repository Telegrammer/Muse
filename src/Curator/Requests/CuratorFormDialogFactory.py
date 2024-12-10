from src.Curator.Requests.CuratorRequestsDialog import CuratorRequestsDialog
from src.Curator.Requests.RequestWidget import RequestWidget
from src.Curator.Requests.ActsWidget import ActsWidget
from src.Emitters import TupleEmitter


class CuratorFormDialogFactory:

    def __init__(self, donators_requests: list[tuple[str]], mode: str):
        self.__donators_requests = donators_requests
        self.__request_mode = mode

    def __call__(self, table_attributes: list[tuple], parent_signal: TupleEmitter = TupleEmitter(None)):
        dialog_form = CuratorRequestsDialog()
        for request_id, donator_id, donator_info, formDate, description in self.__donators_requests:
            if self.__request_mode == 'unchecked':
                request_widget = RequestWidget(request_id, parent_signal=parent_signal)
            else:
                request_widget = ActsWidget(request_id, table_attributes, parent_signal=parent_signal)
            request_widget.donatorLineEdit.setText(donator_info)
            request_widget.formDateLineEdit.setText(formDate)
            request_widget.descriptionLineEdit.setText(description)
            dialog_form.add_request_widget(request_widget)
        return dialog_form
