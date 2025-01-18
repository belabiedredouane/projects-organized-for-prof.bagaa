part of 'picker_image_bloc.dart';

@immutable
sealed class PickerImageEvent {}

final class CameraEvent extends PickerImageEvent {}

final class GalleryEvent extends PickerImageEvent {}

final class VoiceEvent extends PickerImageEvent {}

final class VoiceStopEvent extends PickerImageEvent {}

final class VoiceResumeEvent extends PickerImageEvent {}
