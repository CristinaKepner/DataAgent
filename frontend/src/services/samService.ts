import axios from 'axios';

const SAM_API_URL = '/api/sam';

export const samService = {
  async predictMasks(imageData: Blob): Promise<any> {
    const formData = new FormData();
    formData.append('image', imageData);
    
    const response = await axios.post(`${SAM_API_URL}/predict`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    
    return response.data.masks;
  },

  async refineMask(maskData: any): Promise<any> {
    const response = await axios.post(`${SAM_API_URL}/refine`, maskData);
    return response.data.refinedMask;
  }
};