# 第 12～19 章來源與教學對照

PDF 頁碼均由各檔第一頁起算；第 17 章原圖取自線上完整章節，其正文始於 PDF 第 5 頁。書本是主線，PPTX 僅補充對應內容。

## 主教材覆蓋

| 來源 | 教學小節 | 投影片 |
| --- | --- | --- |
| [Ch.12 PDF 1–17](<../../../book/CHAPTER 12 Deep Computer Vision Using Convolutional Neural Networks.pdf>) | 視覺皮質、感受野、卷積、padding、通道、pooling、PyTorch尺寸 | [14：卷積神經網路：影像特徵與架構](../../14_卷積神經網路_影像特徵與架構.md) |
| [Ch.12 PDF 17–37](<../../../book/CHAPTER 12 Deep Computer Vision Using Convolutional Neural Networks.pdf>) | CNN、LeNet、AlexNet、增強、GoogLeNet、ResNet、Xception、SENet與其他架構 | [14：卷積神經網路：影像特徵與架構](../../14_卷積神經網路_影像特徵與架構.md) |
| [Ch.12 PDF 37–48](<../../../book/CHAPTER 12 Deep Computer Vision Using Convolutional Neural Networks.pdf>) | 選模型、GPU RAM、RevNet、ResNet實作、預訓練與遷移 | [15：電腦視覺：遷移學習與偵測分割](../../15_電腦視覺_遷移學習與偵測分割.md) |
| [Ch.12 PDF 48–66](<../../../book/CHAPTER 12 Deep Computer Vision Using Convolutional Neural Networks.pdf>) | 定位、FCN、YOLO、mAP、追蹤、分割、其他卷積與活動 | [15：電腦視覺：遷移學習與偵測分割](../../15_電腦視覺_遷移學習與偵測分割.md) |
| [Ch.13 PDF 1–18](<../../../book/CHAPTER 13 Processing Sequences Using RNNs and CNNs.pdf>) | RNN狀態、序列對齊、BPTT、運量、季節性、ARMA、資料窗 | [16：序列模型：RNN 與時間序列預測](../../16_序列模型_RNN與時間序列預測.md) |
| [Ch.13 PDF 18–29](<../../../book/CHAPTER 13 Processing Sequences Using RNNs and CNNs.pdf>) | 線性與深層RNN、多變量、多步與seq2seq預測 | [16：序列模型：RNN 與時間序列預測](../../16_序列模型_RNN與時間序列預測.md) |
| [Ch.13 PDF 29–42](<../../../book/CHAPTER 13 Processing Sequences Using RNNs and CNNs.pdf>) | 梯度問題、LSTM、GRU、因果Conv1d、WaveNet與活動 | [16：序列模型：RNN 與時間序列預測](../../16_序列模型_RNN與時間序列預測.md) |
| [Ch.14 PDF 1–13](<../../../book/CHAPTER 14 Natural Language Processing with RNNs and Attention.pdf>) | 字元資料窗、embedding、Char-RNN、抽樣；Notebook補stateful | [17：自然語言處理：詞嵌入與注意力](../../17_自然語言處理_詞嵌入與注意力.md) |
| [Ch.14 PDF 13–35](<../../../book/CHAPTER 14 Natural Language Processing with RNNs and Attention.pdf>) | IMDB、BPE／WordPiece／Unigram、padding、雙向RNN、預訓練、Trainer、pipeline、公平性 | [17：自然語言處理：詞嵌入與注意力](../../17_自然語言處理_詞嵌入與注意力.md) |
| [Ch.14 PDF 36–52](<../../../book/CHAPTER 14 Natural Language Processing with RNNs and Attention.pdf>) | Encoder–decoder、teacher forcing、優化、beam search、attention與活動 | [17：自然語言處理：詞嵌入與注意力](../../17_自然語言處理_詞嵌入與注意力.md) |
| [Ch.15 PDF 1–18](<../../../book/CHAPTER 15 Transformers for Natural Language Processing and Chatbots.pdf>) | 架構、位置編碼、MHA、遮罩、FFN、LayerNorm與翻譯 | [18：Transformer：注意力架構與預訓練](../../18_Transformer_注意力架構與預訓練.md) |
| [Ch.15 PDF 18–33](<../../../book/CHAPTER 15 Transformers for Natural Language Processing and Chatbots.pdf>) | BERT架構／預訓練／微調、任務頭、其他encoder模型 | [18：Transformer：注意力架構與預訓練](../../18_Transformer_注意力架構與預訓練.md) |
| [Ch.15 PDF 33–57](<../../../book/CHAPTER 15 Transformers for Natural Language Processing and Chatbots.pdf>) | GPT、Mistral、生成、prompt、聊天、SFT、RLHF、DPO、TRL | [19：大型語言模型：生成與聊天系統](../../19_大型語言模型_生成與聊天系統.md) |
| [Ch.15 PDF 57–66](<../../../book/CHAPTER 15 Transformers for Natural Language Processing and Chatbots.pdf>) | 聊天系統、RAG、工具、MCP、結構化生成、框架、T5／BART與活動 | [19：大型語言模型：生成與聊天系統](../../19_大型語言模型_生成與聊天系統.md) |
| [Ch.16 PDF 1–20](<../../../book/CHAPTER 16 Vision and Multimodal Transformers.pdf>) | 視覺attention、DETR、ViT、DeiT、PVT、Swin、DINO與其他視覺方法 | [20：視覺與多模態 Transformer](../../20_視覺與多模態Transformer.md) |
| [Ch.16 PDF 21–40](<../../../book/CHAPTER 16 Vision and Multimodal Transformers.pdf>) | VideoBERT、ViLBERT、CLIP、DALL·E、Perceiver／IO | [20：視覺與多模態 Transformer](../../20_視覺與多模態Transformer.md) |
| [Ch.16 PDF 40–50](<../../../book/CHAPTER 16 Vision and Multimodal Transformers.pdf>) | Flamingo、BLIP／BLIP-2、其他多模態任務與活動 | [20：視覺與多模態 Transformer](../../20_視覺與多模態Transformer.md) |
| [Ch.17 PDF 1–2（本地）／5–65（線上）](<../../../book/CHAPTER 17 Speeding Up Transformers.pdf>) | KV cache、推測／平行解碼、batching、稀疏／近似注意力、MHA／MQA／GQA／MLA、FlashAttention、MoE、PEFT／LoRA、checkpointing、packing、梯度累積與平行訓練 | [21：Transformer 加速：推論與參數高效微調](../../21_Transformer加速_推論與參數高效微調.md) |
| [Ch.18 PDF 1–21](<../../../book/CHAPTER 18 Autoencoders, GANs, and Diffusion Models.pdf>) | 表示、線性AE／PCA、stacked AE、重建、異常、視覺化、預訓練、tied weights、逐層訓練、conv／去噪／稀疏AE | [22：生成模型：自編碼器、GAN 與擴散](../../22_生成模型_自編碼器GAN與擴散.md) |
| [Ch.18 PDF 21–36](<../../../book/CHAPTER 18 Autoencoders, GANs, and Diffusion Models.pdf>) | VAE、抽樣、KL、離散VAE、VQ-VAE、GAN、DCGAN與mode collapse | [22：生成模型：自編碼器、GAN 與擴散](../../22_生成模型_自編碼器GAN與擴散.md) |
| [Ch.18 PDF 36–46](<../../../book/CHAPTER 18 Autoencoders, GANs, and Diffusion Models.pdf>) | 加噪、噪聲排程、U-Net、DDPM／DDIM、latent diffusion與活動；flow matching只列Notebook選讀 | [22：生成模型：自編碼器、GAN 與擴散](../../22_生成模型_自編碼器GAN與擴散.md) |
| [Ch.19 PDF 1–16](<../../../book/CHAPTER 19 Reinforcement Learning.pdf>) | 互動、Gymnasium、策略、回報、REINFORCE | [23：強化學習：策略、價值與深度 RL](../../23_強化學習_策略價值與深度RL.md) |
| [Ch.19 PDF 16–33](<../../../book/CHAPTER 19 Reinforcement Learning.pdf>) | MDP、Bellman、TD、Q-learning、探索、DQN與改善 | [23：強化學習：策略、價值與深度 RL](../../23_強化學習_策略價值與深度RL.md) |
| [Ch.19 PDF 33–46](<../../../book/CHAPTER 19 Reinforcement Learning.pdf>) | Actor–critic、PPO、Atari、演算法總覽、on/off-policy、環境模型與活動 | [23：強化學習：策略、價值與深度 RL](../../23_強化學習_策略價值與深度RL.md) |
| [附錄A PDF 1–8](<../../../book/Appendix A Autodiff.pdf>) | 手算、有限差分、計算圖、前向模式、對偶數、反向模式、autograd | [24：附錄 A：自動微分與計算圖](../../24_附錄A_自動微分與計算圖.md) |
| [附錄B PDF 1–20](<../../../book/Appendix B Mixed Precision and Quantization.pdf>) | 數值表示、降低精度、AMP、線性量化、PTQ、QAT、bitsandbytes與預量化模型 | [25：附錄 B：混合精度與量化](../../25_附錄B_混合精度與量化.md) |

## 程式來源

所有作者 Notebook 連結固定於同一 commit；下列 Cell 以 0 起算。摘錄經教學縮寫的部分已在投影片註明。

| Notebook | 課堂閱讀區段 |
| --- | --- |
| [12_deep_computer_vision_with_cnns.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/12_deep_computer_vision_with_cnns.ipynb) | 20–43卷積、44–61池化、64 CNN、74 ResidualUnit、78／82預訓練、92–104微調、106定位、125–138偵測與分割 |
| [13_processing_sequences_using_rnns_and_cnns.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/13_processing_sequences_using_rnns_and_cnns.ipynb) | 48 Dataset、58／64 RNN、80多步、87–102 seq2seq、107 LSTM、112 GRU、123因果卷積 |
| [14_nlp_with_rnns_and_attention.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/14_nlp_with_rnns_and_attention.ipynb) | 39 embedding、42 Char-RNN、55–72 stateful、125 tokenizer、134–139情感、161–186 Trainer／pipeline、210–214 attention |
| [15_transformers_for_nlp_and_chatbots.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/15_transformers_for_nlp_and_chatbots.ipynb) | 31位置、35 MHA、39 encoder、46翻譯、57 BERT、70–73 GPT2、117–124 logprob、133–151 TRL |
| [16_vision_and_multimodal_transformers.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/16_vision_and_multimodal_transformers.ipynb) | 20–22 ViT、40–45 DINO、49 CLIP、68–72 Perceiver、73–75 BLIP-2 |
| [17_speeding_up_transformers.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/17_speeding_up_transformers.ipynb) | 18 cache、20推測解碼、22–45稀疏／近似、48／50 MQA／GQA、53 FlashAttention教學、59 LoRA、63梯度累積 |
| [18_autoencoders_gans_and_diffusion_models.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/18_autoencoders_gans_and_diffusion_models.ipynb) | 22線性AE、33 stacked AE、55 tied weights、81稀疏損失、92–93 VAE、104–113離散VAE、116 GAN、124–152擴散 |
| [19_reinforcement_learning.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/19_reinforcement_learning.ipynb) | 21 Gymnasium、40策略、46回報、48 episode、76 DQN、95 actor–critic、110 PPO |
| [Appendix_A_autodiff.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/Appendix_A_autodiff.ipynb) | 6手算函式、17–23有限差分、32–82 Toy Computation Graph、85–86 autograd |
| [Appendix_B_mixed_precision_and_quantization.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/Appendix_B_mixed_precision_and_quantization.ipynb) | 40 AMP、47量化、48–66 PTQ／QAT、69 bitsandbytes |

作者 Notebook 的 hash 與章節資訊保存在 [notebook_sources.json](notebook_sources.json)。原圖的 PDF 頁、xref 與檔案 hash 保存在 [sources.json](sources.json)。圖片均從原始 PDF 內嵌影像擷取，未重畫。

## 補充素材位置

| 補充素材 | 實際使用方式 |
| --- | --- |
| 07_Convolutional Neural Networks.pptx | CNN、ResNet、增強，補於14／15 |
| 08_Recurrent Neural Networks.pptx | RNN、LSTM、詞袋／Word2Vec、情感與字元生成，補於16／17 |
| 09_POS tagging.pptx | s.2–3詞性例與stemming／lemmatization，補於17 |
| 10_Attention.pptx | s.3–12翻譯瓶頸；s.22–35 QKV；s.38–48位置；s.52–53 LayerNorm；s.71 Reformer |
| 11_Image Captioning.pptx | s.6–16預訓練／encoder；s.14–25資料、decoder與attention，補於15／20 |
| LLM.pptx | token、prompt、情境長度、幻覺與RAG，補於19 |
| 機器學習-10-執行大型語言模型.pptx | BERT／T5／GPT的角色比較，補於18／19；未沿用舊安裝指令 |
| 12_強化學習.pdf | p.13–15 Q-learning數例，補於23；不混用p.10獎勵尺度 |

中文重複版 Attention／Image Captioning 與英數版依內容合併參考，不重複排成新課。

## 本地 MachineLearning2025

| 檔案 | 投影片與用法 |
| --- | --- |
| [06_ANN_from_Scratch_MNIST.py](../../../programs/upstream/MachineLearning2025/06_ANN_from_Scratch_MNIST.py) | 14的MLP／CNN對照；24的手刻backward |
| [04_PCA_from_scratch.py](../../../programs/upstream/MachineLearning2025/04_PCA_from_scratch.py) | 22的線性AE／PCA比較，使用相同前處理 |
| [04_SVD_from_scratch.py](../../../programs/upstream/MachineLearning2025/04_SVD_from_scratch.py) | 22的主子空間對照，明示sigma與U的尺度限制 |

未將本地不存在的CNN／Transformer／diffusion程式標為MachineLearning2025範例。原始程式、PDF與PPTX均保留。

## 適用界線

活動中的數字為書中例或明示的自編例。程式片段以可追蹤的資料流為主，未宣稱本次完成訓練或重現作者效能。技術API採固定來源版本，完整執行前仍需核對Notebook的Setup、模型存取與backend。
