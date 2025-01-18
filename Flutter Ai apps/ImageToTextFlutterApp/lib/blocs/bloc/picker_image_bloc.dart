import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:google_mlkit_text_recognition/google_mlkit_text_recognition.dart';
import 'package:image_picker/image_picker.dart';

part 'picker_image_event.dart';
part 'picker_image_state.dart';

class PickerImageBloc extends Bloc<PickerImageEvent, PickerImageState> {
  File? selectedImage;
  String? scannedText;

  PickerImageBloc() : super(PickerImageInitial()) {
    final flutterTts = FlutterTts();
    int lastSpokenIndex = 0;

    on<PickerImageEvent>((event, emit) async {
      if (event is CameraEvent) {
        try {
          final returnedImage =
              await ImagePicker().pickImage(source: ImageSource.camera);
          if (returnedImage == null) {
            return;
          }
          selectedImage = File(returnedImage.path);
          final inputImage = InputImage.fromFile(selectedImage!);
          final textRecognizer =
              TextRecognizer(script: TextRecognitionScript.latin);
          RecognizedText recognizedText =
              await textRecognizer.processImage(inputImage);
          scannedText = '';
          for (TextBlock block in recognizedText.blocks) {
            for (TextLine line in block.lines) {
              scannedText = '$scannedText${line.text}\n';
            }
          }
          textRecognizer.close();
          emit(CameraSucess());
        } catch (e) {
          emit(CameraFailure());
        }
      } else if (event is GalleryEvent) {
        try {
          final returnedImage =
              await ImagePicker().pickImage(source: ImageSource.gallery);
          if (returnedImage == null) {
            return;
          }
          selectedImage = File(returnedImage.path);
          final inputImage = InputImage.fromFile(selectedImage!);
          final textRecognizer =
              TextRecognizer(script: TextRecognitionScript.latin);
          RecognizedText recognizedText =
              await textRecognizer.processImage(inputImage);
          scannedText = '';
          for (TextBlock block in recognizedText.blocks) {
            for (TextLine line in block.lines) {
              scannedText = '$scannedText${line.text}\n';
            }
          }
          textRecognizer.close();
          emit(GallerySucess());
        } catch (e) {
          emit(GalleryFailure());
        }
      } else if (event is VoiceEvent) {
        flutterTts.setProgressHandler((_, start, end, __) {
          lastSpokenIndex = end;
        });
        await flutterTts.speak(scannedText!);
        emit(StartVoiceSucess());
      } else if (event is VoiceStopEvent) {
        await flutterTts.stop();
        emit(StopVoiceSucess());
      } else if (event is VoiceResumeEvent) {
        String remainingText = scannedText!.substring(lastSpokenIndex);
        await flutterTts.speak(remainingText);
        emit(ResumeVoiceSucess());
      }
    });
  }
}
