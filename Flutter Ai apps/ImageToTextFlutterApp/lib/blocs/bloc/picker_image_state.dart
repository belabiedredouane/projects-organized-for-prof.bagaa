part of 'picker_image_bloc.dart';

@immutable
sealed class PickerImageState {}

final class PickerImageInitial extends PickerImageState {}

final class CameraSucess extends PickerImageState {}

final class CameraFailure extends PickerImageState {}

final class GallerySucess extends PickerImageState {}

final class GalleryFailure extends PickerImageState {}

final class StartVoiceSucess extends PickerImageState {}

final class StopVoiceSucess extends PickerImageState {}

final class ResumeVoiceSucess extends PickerImageState {}
