import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:image2text/blocs/bloc/picker_image_bloc.dart';
import 'package:image2text/widgets/custom_bottun.dart';

class HomeViewBody extends StatelessWidget {
  const HomeViewBody({super.key});

  @override
  Widget build(BuildContext context) {
    return BlocBuilder<PickerImageBloc, PickerImageState>(
      builder: (context, state) {
        if (state is CameraSucess ||
            state is GallerySucess ||
            state is StopVoiceSucess ||
            state is StartVoiceSucess ||
            state is ResumeVoiceSucess) {
          return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 10.0),
            child: ListView(
              physics: const BouncingScrollPhysics(),
              children: [
                const SizedBox(
                  height: 20,
                ),
                Container(
                  margin: const EdgeInsets.only(left: 17),
                  height: 400,
                  width: 380,
                  child: Image.file(
                    BlocProvider.of<PickerImageBloc>(context).selectedImage!,
                  ),
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomButton(
                  text: 'Take Photo From Camera',
                  onPressed: () {
                    BlocProvider.of<PickerImageBloc>(context)
                        .add(CameraEvent());
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomButton(
                  text: 'Take Photo From Gallery',
                  onPressed: () {
                    BlocProvider.of<PickerImageBloc>(context)
                        .add(GalleryEvent());
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomButton(
                  text: 'Reading',
                  onPressed: () {
                    BlocProvider.of<PickerImageBloc>(context).add(VoiceEvent());
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomButton(
                  text: 'Stop Reading',
                  onPressed: () {
                    BlocProvider.of<PickerImageBloc>(context)
                        .add(VoiceStopEvent());
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                CustomButton(
                  text: 'Resume Reading',
                  onPressed: () {
                    BlocProvider.of<PickerImageBloc>(context)
                        .add(VoiceResumeEvent());
                  },
                ),
                const SizedBox(
                  height: 20,
                ),
                SelectableText(
                    BlocProvider.of<PickerImageBloc>(context).scannedText ??
                        'there was an error'),
              ],
            ),
          );
        } else {
          return Column(
            children: [
              const SizedBox(
                height: 20,
              ),
              Container(
                margin: const EdgeInsets.only(left: 17),
                height: 400,
                width: 380,
                child: Image.asset('assets/camera_image.png'),
              ),
              const SizedBox(
                height: 20,
              ),
              CustomButton(
                text: 'Take Photo From Camera',
                onPressed: () {
                  BlocProvider.of<PickerImageBloc>(context).add(CameraEvent());
                },
              ),
              const SizedBox(
                height: 20,
              ),
              CustomButton(
                text: 'Take Photo From Gallery',
                onPressed: () {
                  BlocProvider.of<PickerImageBloc>(context).add(GalleryEvent());
                },
              ),
            ],
          );
        }
      },
    );
  }
}
