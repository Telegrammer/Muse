from src.Curator.Requests.CuratorRequestsDialog import CuratorRequestsDialog
from src.Curator.Requests.RequestWidget import RequestWidget
from src.Emitters import TupleEmitter


class CuratorFormDialogFactory:

    def __init__(self, donators_requests: list[tuple[str]]):
        self.__donators_requests = donators_requests

    def __call__(self, parent_signal: TupleEmitter = TupleEmitter(None)):
        dialog_form = CuratorRequestsDialog()
        for request_id, donator_info, formDate, description in self.__donators_requests:
            request_widget = RequestWidget(request_id, dialog_form.requests, parent_signal)
            request_widget.donatorLineEdit.setText(donator_info)
            request_widget.formDateLineEdit.setText(formDate)
            request_widget.descriptionLineEdit.setText(description)
            dialog_form.add_request_widget(request_widget)
        return dialog_form
