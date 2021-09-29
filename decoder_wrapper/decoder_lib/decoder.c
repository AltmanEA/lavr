#include "decoder.h"

typedef signed char        int8_t;
typedef short              int16_t;
typedef int                int32_t;
typedef long long          int64_t;
typedef unsigned char      uint8_t;
typedef unsigned short     uint16_t;
typedef unsigned int       uint32_t;
typedef unsigned long long uint64_t;

void decode(unsigned char* compressed_data_ptr, unsigned int* result)
{
	int32_t sample, sample_ref;
	uint32_t delta_avg = 0;
	uint32_t delta_shift = 0;
	int16_t sample_cnt;
	uint16_t sample_number;

	compressed_data_ptr++;
	*((uint8_t*)&sample_number + 0) = *(compressed_data_ptr++);
	*((uint8_t*)&sample_number + 1) = *(compressed_data_ptr++);
	*((uint8_t*)&sample + 0) = *compressed_data_ptr++;
	*((uint8_t*)&sample + 1) = *compressed_data_ptr++;
	*((uint8_t*)&sample + 2) = *compressed_data_ptr++;
	*((uint8_t*)&sample + 3) = *compressed_data_ptr++;

	sample_cnt = ((int16_t) *compressed_data_ptr++) - 2;
	compressed_data_ptr++;
	delta_shift = *compressed_data_ptr++;
	delta_avg = *compressed_data_ptr++;
    delta_shift = delta_avg >> 2;
	if (delta_shift < 5) {
		delta_shift=0;
	} else {
		delta_shift -= 5;
	}

	sample_ref = sample;

	if ((sample_cnt == 0) || (sample_cnt == 255))
		return;

    *result++ = sample;
	// Here write sample to output file

	int cnt = 0;
	while (sample_cnt > 0)
	{
		int32_t delta;
		uint8_t code_delta = *compressed_data_ptr++;

		if (code_delta & 0x40) {
			if (code_delta & 0x0F)
				{ delta = ((int32_t)(code_delta & 0x70)) << ((code_delta & 0x0F) + 1); }
			else
				{ delta = (int32_t)(code_delta & 0x30) << 2; }
		} else
			{ delta = ((int32_t)(code_delta & 0x3F)) << delta_shift; }

		uint32_t temp32 = delta;
		uint8_t shift_cnt = 0;
		while (temp32 >>= 1) { shift_cnt++; }
		delta_avg = delta_avg - (delta_avg >> 2) + shift_cnt;
		delta_shift = delta_avg >> 2;
		if (delta_shift < 5) { delta_shift=0; } else { delta_shift -= 5; }

		if (code_delta & 0x80) { delta = -delta; }

		sample_ref = sample_ref + delta;
		sample = sample_ref;

        *result++ = sample;
		// Here write sample to output file

		sample_cnt--;
	}
};
