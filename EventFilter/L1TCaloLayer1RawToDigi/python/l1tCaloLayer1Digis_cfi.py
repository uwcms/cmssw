import FWCore.ParameterSet.Config as cms

l1tCaloLayer1Digis = cms.EDProducer(
    'L1TCaloLayer1RawToDigi',
    fedRawDataLabel = cms.InputTag("rawDataCollector"),
    ecalTPGLabel = cms.InputTag("L1TCaloLayer1", "ECALTPGs"),
    hcalTPGLabel = cms.InputTag("L1TCaloLayer1", "HCALTPGs"),
    FEDIDs = cms.vint32(1354, 1356, 1358),
    verbose = cms.bool(False)
    )
