import React, { useState, useRef } from 'react';
import { samService } from '../services/samService';

const PDFAnnotator: React.FC = () => {
  const [isSAMActive, setSAMActive] = useState(false);
  const canvasRef = useRef<HTMLCanvasElement>(null);

  const handleSAMActivation = async () => {
    if (!canvasRef.current) return;
    
    const canvas = canvasRef.current;
    const imageData = await canvas.toDataURL('image/png');
    
    try {
      const masks = await samService.predictMasks(imageData);
      // 应用SAM预测的mask到标注
      applyMasksToAnnotations(masks);
      setSAMActive(true);
    } catch (error) {
      console.error('SAM预测失败:', error);
    }
  };

  const applyMasksToAnnotations = (masks: any[]) => {
    masks.forEach(mask => {
      const annotation = {
        type: 'polygon',
        points: mask,
        confidence: 0.95 // SAM预测的默认置信度
      };
      addAnnotation(annotation);
    });
  };

  const handleSAMRefine = async (selectedMaskIndex: number) => {
    const maskData = {
      index: selectedMaskIndex,
      image: await canvasRef.current?.toDataURL('image/png')
    };
    
    const refinedMask = await samService.refineMask(maskData);
    updateAnnotation(selectedMaskIndex, refinedMask);
  };

  return (
    <div className="pdf-annotator">
      <canvas ref={canvasRef} />
      <button onClick={handleSAMActivation}>
        {isSAMActive ? 'SAM已激活' : '启用智能拉框'}
      </button>
      {/* ... existing annotation UI ... */}
    </div>
  );
};

export default PDFAnnotator;